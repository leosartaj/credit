#!/usr/bin/env python2

import os
from credit import main, exce
from credit import jsonhelper as jh
from credit.tests import testData as td
import unittest


class Test_total_all_net(unittest.TestCase):

    def setUp(self):
        self.fnum = 10
        self.days = 10
        self.startname = 'test_display'
        self.files = [(self.startname + str(i) + main.SHEETEXT) for i in \
                      range(self.fnum)]
        self.bal = 0
        for index, name in enumerate(self.files):
            money = (index + 1) * 100
            self.bal += money
            fakeDict = td.fakeDict(self.days, money)
            with open(name, 'w') as f:
                f.write(jh.dict_to_json(fakeDict))

    def test_total_all(self):
        num_files = 0
        totals = 0
        for sheetname, total in main.total_all():
            self.assertTrue((sheetname + main.SHEETEXT) in self.files)
            num_files += 1
            totals += total
        self.assertEqual(num_files, self.fnum)
        self.assertTrue(abs(totals - self.bal) < td.ERROR)

    def test_net(self):
        self.assertTrue(abs(main.net() - self.bal) < td.ERROR)

    def tearDown(self):
        for name in self.files:
            os.remove(name)

