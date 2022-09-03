# IPMI-scanner

## How it works

```
usage: IPMI-scanner [-h] [--version]

optional arguments:
  -h, --help     show this help message and exit
  --version, -V  This key allows you to get the current version
```

**Example #1**: Raw result without 'jq'

```bash
> python3 main.py
> {"IPv4": "10.201.7.30", "Mask": "255.255.255.0", "MAC": "a4:bf:01:64:e8:aa", "Gateway": "10.201.7.254", "Channel": "3"}
```

**Example #2**: 

```bash
> python3 main.py | jq
> {
  "IPv4": "10.245.0.11",
  "Channel": "1",
  "Mask": "255.255.255.0",
  "MAC": "00:25:90:8b:cd:cd",
  "Gateway": "10.245.0.254"
}
```

**Example #3**: Empty result

```bash
> python3 main.py | jq
{
  "IPMI-scanner": [
    {}
  ]
}
```
To format and check already modified code, run , but set 's' before running if necessary!
## Code style
⚠️ To format and lint already modified code, run **[./format.sh](format.sh)**, but set **[requirements.txt](requirements.txt)** before running if necessrary

## License

See the [LICENSE](LICENSE) file for license rights and limitations (MIT).
