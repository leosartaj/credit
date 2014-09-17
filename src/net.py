#!/usr/bin/python2

##
# Credit
# https://github.com/leosartaj/credit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

from func import net
import sys

def main():
    if len(sys.argv) == 2: 
        print net(sys.argv[1]) 
    elif len(sys.argv) == 1:
        print net()

if __name__ == '__main__':
    main()
