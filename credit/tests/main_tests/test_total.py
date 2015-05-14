#!/usr/bin/env python2

import os
from credit import main, exce
from credit import jsonhelper as jh
from credit.tests import testData as td
import unittest


class Test_total(unittest.TestCase):

    def setUp(self):
        self.bal = 1000.50
        self.days = 11
        fakeDict = self.fakeDict = td.fakeDict(self.days, self.bal)
        with open(td.fakeSheet, 'w') as f:
            f.write(jh.dict_to_json(fakeDict))

    def test_total_list(self):
        l = td.create_list(self.bal)
        tl = main.total_list(l)
        self.assertTrue(abs(tl - self.bal) < td.ERROR)

    def test_total(self):
        tl = main.total(td.fakeSheet)
        self.assertTrue(abs(tl - self.bal) < td.ERROR)

    def test_total_date(self):
        d = main.timestamp(td.inc_date())
        total_date = main.total_list(self.fakeDict[d])
        tl = main.total(td.fakeSheet, d)
        self.assertTrue(abs(tl - total_date) < td.ERROR)

    def tearDown(self):
        os.remove(td.fakeSheet)
