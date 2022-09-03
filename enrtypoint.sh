#!/bin/sh

if [ "$1" = "-V" ] || [ "$1" = "--version" ]; then
	python3 main.py -V
elif [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
	python3 main.py -h
else
	python3 main.py | jq
fi
