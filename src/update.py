#!/usr/bin/python2

##
# Credit
# https://github.com/MnC-69/credit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

from func import update
import sys

def main():
    if len(sys.argv) == 4: 
        update(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        update(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
