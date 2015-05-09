#!/usr/bin/env python2

from credit import __version__

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name = 'credit',
    version = __version__,
    author = 'Sartaj Singh',
    author_email = 'singhsartaj94@gmail.com',
    description = ('Manage your finances easily and effectively'),
    long_description = open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read(),
    license = 'MIT',
    keywords = 'expenditure finances ledger',
    url = 'http://github.com/leosartaj/credit',
    packages=find_packages(),
    scripts=['bin/credit'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
)
