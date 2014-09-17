#!/usr/bin/python2

##
# Credit
# https://github.com/leosartaj/credit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

from func import display
import sys

def main():
    if len(sys.argv) == 2: 
        print display(sys.argv[1])
    elif len(sys.argv) == 1:
        print display()

if __name__ == '__main__':
    main()



