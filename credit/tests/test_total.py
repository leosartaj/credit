#!/usr/bin/env python2

import os
from credit import main, exce
from credit import jsonhelper as jh
import testData as td
import unittest


class TestTotal(unittest.TestCase):

    def setUp(self):
        self.bal = 1000.50
        self.days = 11
        fakeDict = self.fakeDict = td.fakeDict(self.days, self.bal)
        with open(td.fakeSheet, 'w') as f:
            f.write(jh.dict_to_json(fakeDict))

    def test_total_list(self):
        l = td.create_list(self.bal)
        tl = main.total_list(l)
        self.assertTrue(abs(tl - self.bal) < 0.0001)

    def test_total(self):
        tl = main.total(td.fakeSheet)
        self.assertTrue(abs(tl - self.bal) < 0.0001)

    def tearDown(self):
        os.remove(td.fakeSheet)
