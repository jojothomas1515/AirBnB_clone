#!/usr/bin/python3
"""Test for Basemodel"""

import unittest

from sqlalchemy import false
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        del self.b1
        del self.b2

    def test_if_same_id(self):
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_not_same_object(self):
        self.assertIsNot(self.b1, self.b2)

