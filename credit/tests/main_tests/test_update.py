#!/usr/bin/env python2

import os
from credit import main, exce
from credit import jsonhelper as jh
from datetime import date, timedelta
from credit.tests import testData as td
import unittest


class Test_update(unittest.TestCase):

    def setUp(self):
        self.bal = 100
        fakeDict = self.fakeDict = td.fakeDict(0, 0)
        with open(td.fakeSheet, 'w') as f:
            f.write(jh.dict_to_json(fakeDict))

    def test_update(self):
        d = main.timestamp(date.today() + timedelta(days=1))
        self.fakeDict[d] = [self.bal]
        main.update(td.fakeSheet, d, self.bal)
        self.assertEqual(main.readSheet(td.fakeSheet), self.fakeDict)

    def tearDown(self):
        os.remove(td.fakeSheet)
