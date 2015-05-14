#!/usr/bin/env python2

import os
from credit import main, exce
from credit.tests import testData as td
import unittest


class Test_deleteSheet(unittest.TestCase):

    def setUp(self):
        with open(td.fakeSheet, 'w') as f:
            f.write('')

    def test_deleteSheet(self):
        main.deleteSheet(td.fakeSheet)
        self.assertFalse(main.fileExists(td.fakeSheet))

    def test_saveSheet_no_sheet(self):
        self.assertRaises(exce.CreditSheetError, main.deleteSheet, \
                            td.dummySheet)

    def tearDown(self):
        if main.fileExists(td.fakeSheet):
            os.remove(td.fakeSheet)
