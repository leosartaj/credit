#!/usr/bin/python2

from func import reset
import sys

def main():
    if len(sys.argv) == 3:
        reset(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        reset(sys.argv[1])

if __name__ == '__main__':
    main()


