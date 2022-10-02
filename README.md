# qrcode-script

This repository could be used for converting a word to QR code.

## Requirement

- Windows 10
- [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop) 4.2.0

## How to use

1. Execute the following command. TEXT is the word which would be converted to QR code, and FILE_NAME is the output name.
```
$ docker-compose run --rm -e TEXT={Your text like URL} -e FILE_NAME={File name} qrcode
```
2. Search the directory, "app/output" for the output png file.
