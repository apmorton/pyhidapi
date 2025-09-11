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

## FreeBSD
Binary distributions are available.

```
pkg install -g 'py3*-hid'
```

# Sample usage code

The details about a HID device can be printed with following code:

```python
import hid

vid = 0x046d	# Change it for your device
pid = 0xc534	# Change it for your device

with hid.Device(vid, pid) as h:
	print(f'Device manufacturer: {h.manufacturer}')
	print(f'Product: {h.product}')
	print(f'Serial Number: {h.serial}')
```


Sending and receiving data can be done with following code:

```python
import sys
import hid

vendor_id     = 0x4335
product_id    = 0x0002

usage_page    = 0xFF60
usage         = 0x61
report_length = 32

def get_raw_hid_interface():
    device_interfaces = hid.enumerate(vendor_id, product_id)
    raw_hid_interfaces = [i for i in device_interfaces if i['usage_page'] == usage_page and i['usage'] == usage]

    if len(raw_hid_interfaces) == 0:
        return None

    interface = hid.Device(path=raw_hid_interfaces[0]['path'])

    print(f"Manufacturer: {interface.manufacturer}")
    print(f"Product: {interface.product}")

    return interface

def send_raw_report(data):
    interface = get_raw_hid_interface()

    if interface is None:
        print("No device found")
        sys.exit(1)

    request_data = [0x00] * (report_length + 1) # First byte is Report ID
    request_data[1:len(data) + 1] = data
    request_report = bytes(request_data)

    print("Request:")
    print(request_report)

    try:
        interface.write(request_report)

        response_report = interface.read(report_length, timeout=1000)

        print("Response:")
        print(response_report)
    finally:
        interface.close()

if __name__ == '__main__':
    send_raw_report([
        0x41
    ])
```
Source: https://docs.qmk.fm/features/rawhid#simple-example

