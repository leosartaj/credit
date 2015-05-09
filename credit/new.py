#!/usr/bin/python2

from func import newAcc
import sys

def main():
    if len(sys.argv) == 3:
        newAcc(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        newAcc(sys.argv[1])

if __name__ == '__main__':
    main()

