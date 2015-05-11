"""
Tests related data and helper functions
"""

from credit import main
from credit import jsonhelper as jh
from random import randint, shuffle
from datetime import date, timedelta

dummySheet = 'dummy' + main.SHEETEXT
fakeSheet = 'fake' + main.SHEETEXT


def fakeDict(num=100, bal=100):
    json_dict = {main.INIT: main.timestamp()}
    if num > 0:
        add_lists(json_dict, num, bal)
    return json_dict


def add_lists(json_dict, num, bal, d=date.today()):
    """
    adds 'num' number of lists
    having a grand total equal to bal
    """
    list_bal = float(bal) / num
    for i in range(1, num + 1):
        d += timedelta(days=i)
        json_dict[main.timestamp(d)] = create_list(list_bal)
    return json_dict


def create_list(bal, entries=randint(10, 15)):
    """
    Creates list with a total equal to 'bal'
    """
    entry = float(bal) / entries
    l = [str(entry) for i in range(2 * entries)]
    l.extend([str(-entry) for i in range(entries)])
    return l
