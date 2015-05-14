#!/usr/bin/python2

"""
Main module
"""

import os, math
from datetime import date
import jsonhelper as jh
import printing as pr
import exce


ROOT = os.path.expanduser('~/.credit')
SHEETEXT = '.sheet' # extension of a credit sheet
INIT = 'created'


def bootstrap(root=ROOT):
    """
    setups everything required
    Creates the root directory
    """
    if not dirExists(root):
        createDir(root)


def createDir(dire):
    """
    Creates a new directory
    """
    os.makedirs(dire)


def pDir():
    """
    gives the present working directory
    """
    return os.getcwd()


def sheetPath(sheetname, ext=SHEETEXT, root=ROOT):
    """
    returns the path of the sheet
    """
    return full_path_to(sheetname + ext, root)


def full_path_to(fName, dire=pDir()):
    """
    joins the filename and the directory path
    """
    path = os.path.join(dire, fName)
    return path


def dirExists(fPath):
    """
    Check if a dir exists
    """
    if os.path.isdir(fPath):
        return True
    return False


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


def update(fPath, date, value):
    """
    update to file
    """
    json_dict = readSheet(fPath)
    json_dict = jh.update_dict(json_dict, date, value)
    saveSheet(fPath, json_dict)


def total_list(l):
    """
    converts the list to list of floats
    Sums up the list
    """
    l = map(float, l)
    return math.fsum(l)


def total(fPath, date=None):
    """
    finds the total balance in a credit sheet
    if date is not None, totals for that specific date
    """
    json_dict = readSheet(fPath)

    val = 0.0
    for key in json_dict:
        if date == None or date == key:
            if not key == INIT:
                val += total_list(json_dict[key])
    return val


def total_all(dire=pDir(), date=None):
    """
    Total of all sheets
    if date is not None, totals for that specific date
    """
    for sheetname in sheetNames(dire):
        fPath = full_path_to(sheetname + SHEETEXT, dire)
        yield sheetname, total(fPath, date)


def net(dire=pDir(), date=None, ignore=['me']):
    """
    Get the net credit accounting all files
    if date is not None, calculates net total for that specific date
    """
    net = 0.0
    for sheet, bal in total_all(dire, date):
        if not sheet in ignore:
            net += bal
    return net


def sheetNames(dire=pDir()):
    """
    Generates the name of credit sheets
    """
    for filename in os.listdir(dire):
        name, ext = os.path.splitext(filename)
        if ext == SHEETEXT:
            yield name


def sheetReport(dire=ROOT, date=None, totals=True):
    """
    Displays the sheet names alongwith totals
    if totals is set to True
    if date is not None, shows total for only that date
    """
    if totals:
        l = [(sheetname, str(total)) for sheetname, total in \
             total_all(dire, date)]
        for idx, val in enumerate(l):
            l[idx] = pr.printkv(val[0], val[1])
    else:
        l = [sheetname for sheetname in sheetNames(dire)]
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


def report(dire=ROOT, date=None):
    """
    Gives a full report
    """
    rep = sheetReport(dire, date, totals=True)
    rep += 2*pr.DELIMITER
    rep += pr.printkv('net', str(net(dire, date)))
    return rep


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
