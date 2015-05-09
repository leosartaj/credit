#!/usr/bin/env python2

import os
from credit import main
import testData as td
import unittest


class TestnewSheet(unittest.TestCase):

    def test_create_newSheet(self):
        self.assertFalse(main.fileExists(td.dummySheet))
        main.newSheet(td.dummySheet)
        self.assertTrue(main.fileExists(td.dummySheet))

    def tearDown(self):
        os.remove(td.dummySheet)
