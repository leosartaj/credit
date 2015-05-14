"""
Handles printing
"""

import os
import main


KEYSEP = ' -> '
LSEP = ' '
DELIMITER = os.linesep


def printkv(key, val, sep=KEYSEP):
    """
    formats key, value
    prints key, value
    """
    return key + KEYSEP + val


def printlist(l, sep=LSEP):
    """
    Joins a list with the separator sep
    """
    return sep.join(l)


def plusminus(l, sep=LSEP):
    """
    Makes the numbers pretty
    """
    for idx, ele in enumerate(l):
        if ele[0] == '-':
            temp = ele[0] + sep + ele[1:]
        elif ele[0] == '+':
            temp = '+' + sep + ele[1:]
        else:
            temp = '+' + sep + ele
        l[idx] = temp
    return l


def print_dict(json_dict, keysep=KEYSEP, valsep=LSEP, special=[]):
    """
    Knows how to print dictionary obtained by reading a credit sheet
    behaves in a special way for the keys in special
    """
    pdict = ''
    for key in special:
        pdict += printkv(key, json_dict[key], keysep)
    for key in json_dict:
        if not key in special:
            pdict += 2*DELIMITER
            tidy = plusminus(json_dict[key], valsep)
            val = printlist(tidy, valsep)
            pdict += printkv(key, val, keysep)
    return pdict
