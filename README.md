# py-unzip

The simplest cli possible to unzip a file on a Windows machine. Created out of pure necessity.

## Dependencies

- Python 2.7

## Build

```
pip install pyinstaller
git clone https://github.com/joeferraro/py-unzip
cd py-unzip
pyinstaller py-unzip.spec --one-file
```

## Usage

```
unzip.exe -z c:\some\zipfile.zip -d c:\some\path
```

py-unzip will unzip `c:\some\zipfile.zip` to `c:\some\path`
