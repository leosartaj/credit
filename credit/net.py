#!/usr/bin/python2

from func import net
import sys

def main():
    if len(sys.argv) == 2:
        print net(sys.argv[1])
    elif len(sys.argv) == 1:
        print net()

if __name__ == '__main__':
    main()
