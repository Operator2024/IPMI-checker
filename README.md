# IPMI-scanner

## How it works

```
usage: IPMI-scanner [-h] [--version]

optional arguments:
  -h, --help     show this help message and exit
  --version, -V  This key allows you to get the current version
```

**Example #1**:

```bash
> docker build -t ipmi-scanner .
> docker run -ti --rm --privileged ipmi-scanner
```

```json
> {
  "IPv4": "10.245.0.11",
  "Channel": "1",
  "Mask": "255.255.255.0",
  "MAC": "00:25:90:8b:cd:cd",
  "Gateway": "10.245.0.254"
}
```

**Example #2**: Empty result

```bash
> docker build -t ipmi-scanner .
> docker run -ti --rm --privileged ipmi-scanner
```

```json
{
  "IPMI-scanner": [
    {}
  ]
}
```

## Code style
⚠️ To format and lint already modified code, run **[./format.sh](format.sh)**, but set **[requirements.txt](requirements.txt)** before running if necessrary

## License

See the [LICENSE](LICENSE) file for license rights and limitations (MIT).
