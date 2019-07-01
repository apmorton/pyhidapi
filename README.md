# Installing pyhidapi
pyhidapi is available on [PyPI](https://pypi.org/project/hid/) and can be installed using pip.
```
pip install hid
```

pyhidapi is dependant upon the [hidapi library](https://github.com/libusb/hidapi), which must be installed separately.

# Installing hidapi

## Linux
Installation procedures vary depending on your distribution.

### Arch Linux
Binary distributions are available in the community repository.

1. Enable the community repository in `/etc/pacman.conf`
```
[community]
Include = /etc/pacman.d/mirrorlist
```
2. Install hidapi
```
pacman -Sy hidapi
```

### CentOS/RHEL
Binary distributions are available through [EPEL](https://fedoraproject.org/wiki/EPEL).
```
yum install hidapi
```

### Fedora
Binary distributions are available.
```
dnf install hidapi
```

### Ubuntu/Debian
Binary distributions are available.

```
apt install libhidapi-hidraw0
```
or
```
apt install libhidapi-libusb0
```

### Others
Binary distributions may be available in your package repositories. If not, you can build from source as described [in the libusb/hidapi README](https://github.com/libusb/hidapi#build-instructions).

## Windows
Installation procedure for Windows is described [in the libusb/hidapi README](https://github.com/libusb/hidapi#building-on-windows)

Binary distributions are provided by [libusb/hidapi](https://github.com/libusb/hidapi/releases)

## OSX
There are currently no official binary distributions for Mac, so you must build hidapi yourself.

Installation instructions are described [in the libusb/hidapi README](https://github.com/libusb/hidapi#mac)

You can also use brew:
```
brew install hidapi
```
It should be noted that at this time, brew still uses the old signal11 repository which has long since been abandond.
See [Homebrew/homebrew-core#41122](https://github.com/Homebrew/homebrew-core/pull/41122).
