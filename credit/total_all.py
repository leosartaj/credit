#!/usr/bin/python2

from func import total_all
import sys

def main():
    if len(sys.argv) == 2:
        total_all(sys.argv[1])
    elif len(sys.argv) == 1:
        total_all()

if __name__ == '__main__':
    main()

