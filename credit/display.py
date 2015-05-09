#!/usr/bin/python2

from func import display
import sys

def main():
    if len(sys.argv) == 2:
        print display(sys.argv[1])
    elif len(sys.argv) == 1:
        print display()

if __name__ == '__main__':
    main()
