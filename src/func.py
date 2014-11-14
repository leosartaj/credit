#!/usr/bin/python2
##
# Credit
# https://github.com/leosartaj/credit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# Various helper functions

import os, time
from time import strftime

def pDir():
    """
    gives the present working directory
    """
    return os.getcwd()

def fileExists(fName, dire=pDir()):
    """
    Check if a file exists
    """
    if os.path.isfile(os.path.join(dire, fName)):
        return True
    return False

def timestamp():
    """
    gives a formatted timestamp
    """
    return strftime("%x")

def newAcc(fName, dire=pDir()):
    if fileExists(fName, dire):
        raise Exception('Account Exists')
    with open(os.path.join(dire, fName), 'w') as f:
        f.write('[Created -> ' + timestamp() + ']\n')

def update(fName, num, dire=pDir()):
    """
    update to file
    """
    if not fileExists(fName, dire):
        raise Exception('No such account')

    with open(os.path.join(dire, fName), 'a+') as f:
        f.seek(0, 0)
        b = 0
        for line in f:
            if line[0] == '[' and timestamp() == line[1:-2]: # find the correct date
                b = 1
                break
        if b == 0: # if no such date add a new one
            f.write('\n[' + timestamp() + ']\n')
        if num[0] == '+':
            f.write(' + ' + num[1:])
        elif num[0] == '-':
            f.write(' - ' + num[1:])
        else:
            f.write(' + ' + num)

def display(dire=pDir()):
    """
    gives the list of files
    """
    accs = ''
    for filename in os.listdir(dire):
        accs += filename + ' '
    return 'Accounts -> ' + accs

def total(fName, dire=pDir()):
    """
    finds the total balance with a particular file
    """
    if not fileExists(fName, dire):
        raise Exception('No such account')
    with open(os.path.join(dire, fName), 'r') as f:
        net = 0
        for line in f:
            if line[0] == '[':
                continue
            line = line.replace('\n', '')
            line = line.split(' ')
            for i in range(1, len(line)):
                if line[i] == '+' or line[i] == '-':
                    continue
                if line[i - 1] == '+':
                    net += float(line[i])
                else:
                    net -= float(line[i])
    return net

def total_all(dire=pDir()):
    """
    Total of all accounts
    """
    for filename in os.listdir(dire):
        print filename, '->', total(filename, dire)

def net(dire=pDir()):
    """
    Get the net credit accounting all files
    """
    net = 0
    for filename in os.listdir(dire):
        if filename != 'me':
            net += total(filename, dire)
    return net

def display_acc(fName, dire=pDir()):
    """
    displays the content of a file
    """
    if not fileExists(fName, dire):
        raise Exception('No such account')
    with open(os.path.join(dire, fName), 'r') as f:
        acc = ''
        for line in f:
            acc += line
    return acc

def reset(fName, dire=pDir()):
    """
    Reset an account to 0
    """
    if not fileExists(fName, dire):
        raise Exception('No such account')
    delete(fName, dire)
    newAcc(fName, dire)

def delete(fName, dire=pDir()):
    """
    delete an account
    """
    if not fileExists(fName, dire):
        raise Exception('No such account')
    os.remove(os.path.join(dire, fName))
