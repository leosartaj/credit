#!/usr/bin/python2

from func import total
import sys

def main():
    if len(sys.argv) == 3:
        print total(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        print total(sys.argv[1])

if __name__ == '__main__':
    main()

