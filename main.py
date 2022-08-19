#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import os

__version__ = os.environ["VER"] if os.environ.get("VER") else "0.1.0"

__author__ = "Vladimir Belomestnykh aka Operator2024"

__license__ = "MIT"

import argparse
import json
import re
from io import BufferedReader
from subprocess import PIPE, Popen
from typing import Dict, Optional, Text


def parse_ipmi_info(data: Dict, raw_data: bytes) -> Dict:
    result: bytes = raw_data
    for i in result.decode().split("\n"):
        if re.search("IP Address", i):
            if re.search(r"(0.0.0.0|:\s\n)", i):
                return data
            elif re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", i):
                data["IPv4"] = i.split(":")[1].lstrip(" ").rstrip(" ")
                break
            else:
                pass
        else:
            pass
    for j in result.decode().split("\n"):
        if re.search("Subnet Mask", j) and len(data) > 0:
            if re.search(r"(0.0.0.0|:\s\n)", j):
                data["Mask"] = None
            elif re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", j):
                data["Mask"] = j.split(":")[1].lstrip(" ").rstrip(" ")
        elif re.search("Default Gateway IP", j) and len(data) > 0:
            if re.search(r"(0.0.0.0|:\s\n)", j):
                data["Gateway"] = None
            elif re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", j):
                data["Gateway"] = j.split(":")[1].lstrip(" ").rstrip(" ")
        elif re.search("MAC Address", j) and len(data) > 0:
            if re.search(r"(00:00:00:00:00:00|:\s\n)", j):
                data["MAC"] = None
            elif re.search(r".{1,2}:.{1,2}:.{1,2}:.{1,2}:.{1,2}:.{1,2}", j):
                data["MAC"] = re.split(r"\s:", j)[1].lstrip(" ").rstrip(" ")
    return data


def main(channel: Text = "") -> Optional[Dict]:
    storage: Dict[Text, Text] = {}
    result = b""
    if channel is None:
        return None
    proc: Popen[bytes] = Popen(["ipmitool", "lan", "print", channel],
                               shell=False,
                               stdout=PIPE,
                               stderr=PIPE)
    if isinstance(proc.stderr,
                  BufferedReader) and isinstance(proc.stdout, BufferedReader):
        result = proc.stdout.read() + proc.stderr.read()
    if len(result) == 0:
        return None
    else:
        storage = parse_ipmi_info(storage, result)
        if len(storage) > 0:
            storage["Channel"] = channel
        return storage


if __name__ == "__main__":
    description = "IPMI/BMC inventory system aka IPMI-checker"
    parser = argparse.ArgumentParser(prog="IPMI-checker")
    parser.add_argument(
        "--version",
        "-V",
        help="This key allows you to get the current version",
        version=(
            f"{description}, {__license__} license, {__author__}, version:"
            f" {__version__} "
        ),
        action="version",
    )
    args = parser.parse_args()
    if len(args._get_args()) > 0:
        parser.print_help()
    else:
        Next = False
        ipmi_info = {}
        for i in range(1, 4):
            ipmi_info: Optional[Dict] = main(str(i))
            if ipmi_info is not None:
                if len(ipmi_info) == 0:
                    Next = True
            if not Next:
                break
        if isinstance(ipmi_info, dict):
            print(json.dumps(ipmi_info))
