#!/usr/bin/python3
"""Test for Basemodel"""
import os
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import pathlib as pl


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

    def test_isinstance(self):
        self.assertIsInstance(self.b1, BaseModel)
        self.assertIsInstance(self.b2, BaseModel)

    def test_save_method(self):
        test_time = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(test_time, self.b1.updated_at)

    def test_model_attributes(self):
        li = ['id', 'created_at', 'updated_at']
        self.assertListEqual(li, list(self.b1.__dict__.keys()))
        li = li + ['name']
        self.b1.name = "victoria"
        self.assertListEqual(li, list(self.b1.__dict__.keys()))

    def test_model_from_dictionary(self):
        self.b1.name = "Jojo"
        b1_json = self.b1.to_dict()
        new_model = BaseModel(**b1_json)
        self.assertEqual(new_model.id, self.b1.id)
        self.assertEqual(new_model.created_at, self.b1.created_at)
        self.assertEqual(new_model.updated_at, self.b1.updated_at)
        self.assertEqual(new_model.name, self.b1.name)

    def test_instance_attribute_type(self):
        self.assertIsInstance(self.b1.id, str)
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)
