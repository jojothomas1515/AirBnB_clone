#!/usr/bin/python3
"""Test for Basemodel"""
import os
import unittest
from models.base_model import BaseModel
from models import storage
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


class TestBaseModelAndFileStorage(unittest.TestCase):

    def setUp(self):
        storage._FileStorage__file_path = 'test.json'
        storage._FileStorage__objects = {}
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        del self.b1
        del self.b2

        if pl.Path("test.json").is_file():
            os.remove("test.json")

    def test_json_file_existence(self):
        self.b1.save()
        self.assertTrue(pl.Path("test.json").is_file())

    def test_json_file_contains_info(self):
        self.b2.name = "Jojo Thomas"
        self.b2.project_partner_name = "Victoria Oluwabunmi Olabode"
        self.b2.save()
        test_str: str = ""
        with open('test.json', 'r', encoding='utf-8') as fp:
            test_str = fp.read()
        my_re = r"(BaseModel)\.({})".format(self.b2.id)
        self.assertRegex(test_str, expected_regex=my_re)
        self.assertRegex(test_str, expected_regex="(Jojo Thomas)")
        self.assertRegex(test_str, expected_regex="(Victoria Oluwabunmi Olabode)")

    def test_double_save(self):
        self.b1.collab_count = 2
        self.b1.save()
        self.b1.name = "Jojo"
        self.b1.save()
        test_str: str = ""
        with open('test.json', 'r', encoding='utf-8') as fp:
            test_str = fp.read()

        self.assertRegex(test_str, expected_regex="\"(collab_count)\"[:\s]+(2)")
        self.assertRegex(test_str, expected_regex="\"(name)\"[:\s]{2}\"(Jojo)\"")

    # Todo: write a testcase for all
    # Todo: testcase for instance loaded from file
