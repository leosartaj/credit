#!/usr/bin/python2

"""
Main module
"""

import os, time
import jsonhelper as jh
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


def format_date(d, form="%d/%m/%y"):
    """
    formats dates
    """
    return d.strftime(form)


def timestamp():
    """
    gives a formatted timestamp
    """
    today = time.date.today()
    return format_date(today)


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
        json_str = dict_to_json(json_dict)
        f.write(json_str)


def newSheet(fPath):
    if fileExists(fPath):
        raise exce.CreditSheetExists('Credit sheet Exists')

    data = {INIT: timestamp()}
    with open(fPath, 'w') as f:
        f.write(jh.dict_to_json(data))


def display(dire=pDir()):
    """
    Generates the name of credit sheets
    """
    for filename in os.listdir(dire):
        if os.path.splitext(filename)[1] is SHEETEXT:
            yield filename


def update(fPath, field, value):
    """
    update to file
    """
    json_dict = readsheet(fPath)
    json_dict = jh.update_dict(json_dict, field, value)
    saveSheet(fPath, json_dict)


def total_list(l):
    """
    Sums up a list
    """
    l = map(float, l)
    return sum(l)


def total(fPath):
    """
    finds the total balance in a credit sheet
    """
    json_dict = readsheet(fPath)

    val = 0.0
    for key in json_dict:
        if not key is INIT:
            val += total_list(json_dict[key])
    return val


def total_recurr(dire=pDir()):
    """
    Total of all sheets
    """
    for filename in os.listdir(dire):
        fPath = full_path_to(filename, dire)
        creditSheet = os.path.splitext(filename)[0]
        yield filename, total(fPath)


def net(dire=pDir(), ignore=['me']):
    """
    Get the net credit accounting all files
    """
    net = 0.0
    for sheet, bal in total_recurr(dire):
        if not sheet in ignore:
            net += bal
    return net


def displaySheet(fPath):
    """
    displays the content of a sheet
    """
    json_dict = readsheet(fPath)
    val = ''
    for key in json_dict:
        val += key + KEYSEP
        val += VALSEP.join(json_dict[key])
        val += '\n'
    return val


def deleteSheet(fPath):
    """
    delete a credit sheet
    """
    if not fileExists(fPath):
        raise exce.CreditSheetError('No such credit sheet')
    os.remove(fPath)


def reset(fPath):
    """
    Reset(recreate) a credit sheet
    """
    if not fileExists(fPath):
        raise exce.CreditSheetError('No such credit sheet')
    deleteSheet(fPath)
    newSheet(fPath)
