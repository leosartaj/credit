#!/usr/bin/env python2

import os
from credit import main, exce
from credit import jsonhelper as jh
from credit.tests import testData as td
import unittest


class Test_resetSheet(unittest.TestCase):

    def setUp(self):
        fakeDict = self.fakeDict = td.fakeDict()
        with open(td.fakeSheet, 'w') as f:
            f.write(jh.dict_to_json(fakeDict))

    def test_resetSheet(self):
        self.assertEqual(main.readSheet(td.fakeSheet), self.fakeDict)
        main.resetSheet(td.fakeSheet)
        self.assertEqual(main.readSheet(td.fakeSheet), td.fakeDict(0, 0))

    def test_resetSheet_no_sheet(self):
        self.assertRaises(exce.CreditSheetError, \
                            main.resetSheet, td.dummySheet)

    def tearDown(self):
        os.remove(td.fakeSheet)
