#!/usr/bin/env python2

import os
from credit import main, exce
from credit import jsonhelper as jh
import testData as td
import unittest


class TestreadSheet(unittest.TestCase):

    def setUp(self):
        fakeDict = self.fakeDict = td.fakeDict()
        with open(td.fakeSheet, 'w') as f:
            f.write(jh.dict_to_json(fakeDict))

    def test_readSheet(self):
        self.assertEqual(main.readSheet(td.fakeSheet), self.fakeDict)

    def test_readSheet_no_sheet(self):
        self.assertRaises(exce.CreditSheetError, \
                            main.readSheet, td.dummySheet)

    def tearDown(self):
        os.remove(td.fakeSheet)
