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

def update(fName, num, method='add'):
    """
    update a file
    """
    f = open(fName, 'a')
    if method == 'sub':
        f.write(' - ' + str(num))
    else:
        f.write(' + ' + str(num))
    f.close()

#update('new', '10')
#update('new', '10', 'sub')
#update('new', '10')

def display():
    """
    gives the list of files
    """
    l = []
    for item in os.walk(pDir()):
        l.append(item)
    accs = ''
    for acc in l[0][2]:
        accs += acc + ' '
    return 'Accounts -> ' + accs

#print display()

def total(fName):
    """
    finds the total balance with a particular file
    """
    f = open(fName, 'r')
    for line in f:
        line = line.replace('\n', '')
        line = line.split(' ')
        net = 0
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

def display_acc(fName):
    """
    displays the content of a file
    """
    f = open(fName, 'r')
    acc = fName + ' ->'
    for line in f:
        acc += line
    f.close()
    return acc

#print display_acc('new')

def rem_last(fName):
    """
    remove the last entry from file
    """
    f = open(fName, 'r')
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
