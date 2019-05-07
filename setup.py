from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()


version = '1.0.2'

setup(
    name='hid',
    version=version,
    description='ctypes bindings for hidapi',
    long_description=README,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    author='Austin Morton',
    author_email='amorton@juvsoft.com',
    url='https://github.com/apmorton/pyhidapi',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    test_suite='nose.collector'
)
