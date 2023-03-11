#!/usr/bin/python3
"""Test for Basemodel"""
import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
import pathlib as pl


class FileStorage(unittest.TestCase):
    """Testing file storage"""

    def setUp(self):
        """execute before each test"""
        storage._FileStorage__file_path = 'test.json'
        storage._FileStorage__objects = {}
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        """Execute after each test"""
        del self.b1
        del self.b2

        if pl.Path("test.json").is_file():
            os.remove("test.json")

    def test_json_file_existence(self):
        """If json file exist."""
        self.b1.save()
        self.assertTrue(pl.Path("test.json").is_file())

    def test_json_file_contains_info(self):
        """if json file contains the attribute info."""
        self.b2.name = "Jojo Thomas"
        self.b2.project_partner_name = "Victoria Oluwabunmi Olabode"
        self.b2.save()
        test_str: str = ""
        with open('test.json', 'r', encoding='utf-8') as fp:
            test_str = fp.read()
        my_re = r"(BaseModel)\.({})".format(self.b2.id)
        self.assertRegex(test_str, expected_regex=my_re)
        self.assertRegex(test_str, expected_regex="(Jojo Thomas)")
        self.assertRegex(test_str,
                         expected_regex="(Victoria Oluwabunmi Olabode)")

    def test_double_save(self):
        """Test file being save twice , one before editing and after.
        """
        self.b1.collab_count = 2
        self.b1.save()
        self.b1.name = "Jojo"
        self.b1.save()
        test_str: str = ""
        with open('test.json', 'r', encoding='utf-8') as fp:
            test_str = fp.read()

        self.assertRegex(test_str,
                         expected_regex=r"\"(collab_count)\"[:\s]+(2)")
        self.assertRegex(test_str,
                         expected_regex=r"\"(name)\"[:\s]{2}\"(Jojo)\"")

    def test_filestorage_all(self):
        """test file storage all method."""
        self.b1.name = "jojo"
        self.b1.save()
        self.b2.name = "victoria"
        self.b2.save()
        storage._FileStorage__objects = {}
        storage.reload()
        obj_dict = storage.all()
        for key in obj_dict.keys():
            self.assertIn(key.split('.')[1],
                          (self.b1.id, self.b2.id))
        for value in obj_dict.values():
            self.assertIn(value.name, ('jojo', 'victoria'))

    def test_obj_instance_loaded_from_file(self):
        """check for instance loaded from json file."""
        self.b1.save()
        self.b2.save()
        storage._FileStorage__objects = {}
        storage.reload()
        obj_dict = storage.all()
        for value in obj_dict.values():
            self.assertIsInstance(value, BaseModel)

    def test_file_storage_new(self):
        """Test the new method in filestorage"""
        self.b1.save()
        self.b2.save()
        self.assertEqual(len(storage.all()), 2)
        b3 = BaseModel()
        b3.save()
        self.assertEqual(len(storage.all()), 3)


class TestUserAndFileStorage(unittest.TestCase):
    """User and FileStorage Tests."""

    def setUp(self):
        """test"""
        storage._FileStorage__file_path = 'test.json'
        storage._FileStorage__objects = {}
        self.u1 = User()
        self.u2 = User()
        self.u1.first_name = 'Joseph'
        self.u2.first_name = 'Victoria'
        self.u1.last_name = 'Thomas'
        self.u2.last_name = 'Olabodeh'
        self.u1.password = 'megamind'
        self.u2.password = 'root'
        self.u1.email = 'jojothomas1515@gmail.com'
        self.u2.email = 'bhummhie97@gmail.com'

    def tearDown(self):
        """test"""
        del self.u1
        del self.u2

        if pl.Path("test.json").is_file():
            os.remove("test.json")
