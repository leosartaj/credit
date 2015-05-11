#!/usr/bin/env python2

import os
from credit import main, exce
import testData as td
import unittest


class TestnewSheet(unittest.TestCase):

    def setUp(self):
        self.fakeDict = td.fakeDict(0, 0)
        with open(td.dummySheet, 'w') as f:
            f.write('')

    def test_newSheet(self):
        main.newSheet(td.fakeSheet, self.fakeDict)
        self.assertEqual(main.readSheet(td.fakeSheet), self.fakeDict)

    def test_newSheet_sheet_exists(self):
        self.assertRaises(exce.CreditSheetExists, main.newSheet, td.dummySheet,\
                          self.fakeDict)

    def tearDown(self):
        if main.fileExists(td.fakeSheet):
            os.remove(td.fakeSheet)
        os.remove(td.dummySheet)
