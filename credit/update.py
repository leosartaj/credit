#!/usr/bin/python2

from func import update
import sys

def main():
    if len(sys.argv) == 4:
        update(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        update(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
