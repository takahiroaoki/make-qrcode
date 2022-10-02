# qrcode-script

This repository could be used for converting word to QR code.

## Requirement

- Windows 10
- [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop) 4.2.0

## How to use

1. Set environment valiables in docker-compose.yaml. TEXT is the word which would be converted to QR code, and FILE_NAME is the output name.
2. Execute the following command.
```
$ docker-compose run --rm qrcode
```
3. Search the directory, "app/output" for the output png file.