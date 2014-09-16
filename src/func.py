#!/usr/bin/python2

##
# Credit
# https://github.com/MnC-69/credit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# Various helper functions

import os

def pDir():
    """
    gives the present working directory
    """
    return os.getcwd()

def add(fName, num, dire=pDir()):
    """
    add a num to file
    """
    f = open(fName, 'a')
    f.write(' + ' + str(num))
    f.close()

def sub(fName, num, dire=pDir()):
    """
    subtract a num to file
    """
    f = open(fName, 'a')
    f.write(' - ' + str(num))
    f.close()

#add('new', '10')
#sub('new', '10')
#add('new', '10')

def display(dire=pDir()):
    """
    gives the list of files
    """
    accs = ''
    for filename in os.listdir(dire):
        accs += filename + ' '
    return 'Accounts -> ' + accs

#print display()

def total(fName, dire=pDir()):
    """
    finds the total balance with a particular file
    """
    f = open(os.path.join(dire, fName), 'r')
    net = 0
    for line in f:
        line = line.replace('\n', '')
        line = line.split(' ')
        for i in range(1, len(line)):
            if line[i] == '+' or line[i] == '-':
                continue
            if line[i - 1] == '+':
                net += int(line[i])
            else:
                net -= int(line[i])
    f.close()
    return net

#print total('new')

def display_acc(fName, dire=pDir()):
    """
    displays the content of a file
    """
    f = open(os.path.join(dire, fName), 'r')
    acc = fName + ' ->'
    for line in f:
        acc += line
    f.close()
    return acc

print display_acc('new')

def reset(fName, dire=pDir()):
    """
    Reset an account to 0
    """
    f = open(os.path.join(dire, fName), 'w')
    f.close()

#reset('new')
#print display_acc('new')

def rem_last(fName, dire=pDir()):
    """
    remove the last entry from file
    """
    f = open(os.path.join(dire, fName), 'r')
    rline = []
    for line in f:
        rline = line.replace('\n', '')
        rline = rline.split(' ')
    f.close()
    f = open(fName, 'w')
    f.write(' '.join(rline[:-2]))

#rem_last('new')
#print display_acc('new')

def delete(fName):
    """
    delete an account
    """
    os.remove(fName)

#delete('new')
