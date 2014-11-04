# pyhidapi Installation
To install pyhidapi, use the standard module install procedure: `python setup.py install`.  You also need to ensure that you have the required hidapi shared library.  On Linux distributions, this is generally in the repositories (for instance, under Debian you can install either libhidapi-hidraw0 or libhidapi-libusb0 depending on which backend you want to use).

**TODO** I don't know the installation procedure for Windows or other Linux distributions.  If there is anything special needed, please add docs for it here.

# OSX Support
pyhidapi works on OSX, but requires that you first build a shared library.  There may be better ways to do this, but what I did was as follows:

1. Download the latest hidapi release from https://github.com/signal11/hidapi/downloads and unzip
2. Navigate to the mac directory
3. Modify the Makefile to include -fPIC on the CFLAGS line.  My CFLAGS now look like this: `CFLAGS+=-I../hidapi -Wall -g -c -fPIC`
4. Run `make`.  You should now have a hid.o file in this directory.
5. Create the shared library by running: `gcc -shared -o libhidapi-iohidmanager.so hid.o -framework IOKit -framework CoreFoundation`
6. Copy the resulting libhidapi-iohidmanager.so to /usr/local/lib (or somewhere in the libs search path)
7. Install pyhidapi as normal: `python setup.py install`
8. Verify by running python interactively and typing the following lines:
`import hid
hid.enumerate()`
You should see a list of all USB hid devices on your system.

That's it!
