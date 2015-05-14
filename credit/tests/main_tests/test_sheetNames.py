#!/usr/bin/env python2

import os
from credit import main, exce
from credit.tests import testData as td
import unittest


class Test_sheetNames(unittest.TestCase):

    def setUp(self):
        self.fakeDict = td.fakeDict(0, 0)
        self.fnum = 10
        self.startname = 'test_display'
        self.files = [(self.startname + str(i) + main.SHEETEXT) for i in \
                      range(self.fnum)]
        self.files.append(self.startname)
        for name in self.files:
            with open(name, 'w') as f:
                f.write('')

    def test_sheetNames(self):
        fs = [(name + main.SHEETEXT) for name in main.sheetNames()]
        fs.sort()
        self.assertEqual(fs, self.files[:-1])

    def tearDown(self):
        for name in self.files:
            os.remove(name)
