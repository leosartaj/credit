#!/usr/bin/env python2

from credit import jsonhelper as jh
from credit.tests import testData as td
from datetime import date, timedelta
import unittest


class Test_readSheet(unittest.TestCase):

    def setUp(self):
        self.fakeDict = td.fakeDict(10, 10)
        self.field = date.today() + timedelta(days=1)
        self.new_field = date.today() + timedelta(days=100)

    def test_update_dict_new_field(self):
        json_dict = jh.update_dict(self.fakeDict, self.new_field, 10)
        self.fakeDict[self.new_field] = [10]
        self.assertEqual(self.fakeDict, json_dict)

    def test_update_dict_existing_field(self):
        json_dict = jh.update_dict(self.fakeDict, self.field, 10)
        self.fakeDict[self.field].append(10)
        self.assertEqual(self.fakeDict, json_dict)
