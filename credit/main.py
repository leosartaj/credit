#!/usr/bin/python2

"""
Main module
"""

import os, math
from datetime import date
import jsonhelper as jh
import printing as pr
import exce


SHEETEXT = '.sheet' # extension of a credit sheet
INIT = 'created'
KEYSEP = ' -> '
VALSEP = ' '


def pDir():
    """
    gives the present working directory
    """
    return os.getcwd()


def full_path_to(fName, dire=pDir()):
    """
    joins the filename and the directory path
    """
    path = os.path.join(dire, fName)
    return path


def fileExists(fPath):
    """
    Check if a file exists
    """
    if os.path.isfile(fPath):
        return True
    return False


def timestamp(d=date.today(), form="%d/%m/%y"):
    """
    formats dates
    """
    return d.strftime(form)


def readSheet(fPath):
    """
    Reads the json data and returns a dictionary
    """
    if not fileExists(fPath):
        raise exce.CreditSheetError('No such credit sheet')

    with open(fPath) as f:
        json_str = f.read()
        return jh.json_to_dict(json_str)


def saveSheet(fPath, json_dict):
    """
    Saves the json data
    """
    if not fileExists(fPath):
        raise exce.CreditSheetError('No such credit sheet')

    with open(fPath, 'w') as f:
        json_str = jh.dict_to_json(json_dict)
        f.write(json_str)


def newSheet(fPath, json_dict={INIT: timestamp()}):
    if fileExists(fPath):
        raise exce.CreditSheetExists('Credit sheet Exists')

    with open(fPath, 'w') as f:
        f.write(jh.dict_to_json(json_dict))


def display(dire=pDir()):
    """
    Generates the name of credit sheets
    """
    for filename in os.listdir(dire):
        name, ext = os.path.splitext(filename)
        if ext == SHEETEXT:
            yield name


def update(fPath, field, value):
    """
    update to file
    """
    json_dict = readSheet(fPath)
    json_dict = jh.update_dict(json_dict, field, value)
    saveSheet(fPath, json_dict)


def total_list(l):
    """
    converts the list to list of floats
    Sums up the list
    """
    l = map(float, l)
    return math.fsum(l)


def total(fPath):
    """
    finds the total balance in a credit sheet
    """
    json_dict = readSheet(fPath)

    val = 0.0
    for key in json_dict:
        if not key == INIT:
            val += total_list(json_dict[key])
    return val


def total_all(dire=pDir()):
    """
    Total of all sheets
    """
    for sheetname in display(dire):
        fPath = full_path_to(sheetname + SHEETEXT, dire)
        yield sheetname, total(fPath)


def net(dire=pDir(), ignore=['me']):
    """
    Get the net credit accounting all files
    """
    net = 0.0
    for sheet, bal in total_all(dire):
        if not sheet in ignore:
            net += bal
    return net


def displaySheetNames(dire=pDir(), totals=True):
    """
    Displays the sheet names alongwith totals
    if totals is set to True
    """
    if totals:
        l = [(sheetname, str(total)) for sheetname, total in total_all(dire)]
        for idx, val in enumerate(l):
            l[idx] = pr.printkv(val[0], val[1])
    else:
        l = [sheetname for sheetname in display(dire)]
    return pr.printlist(l, pr.DELIMITER)


def displaySheet(fPath, raw=False):
    """
    displays the content of a sheet
    """
    json_dict = readSheet(fPath)
    if raw == False:
        return pr.print_dict(json_dict, special=[INIT])
    else:
        return json_dict


def deleteSheet(fPath):
    """
    delete a credit sheet
    """
    if not fileExists(fPath):
        raise exce.CreditSheetError('No such credit sheet')
    os.remove(fPath)


def resetSheet(fPath):
    """
    Reset(recreate) a credit sheet
    """
    if not fileExists(fPath):
        raise exce.CreditSheetError('No such credit sheet')
    deleteSheet(fPath)
    newSheet(fPath)
