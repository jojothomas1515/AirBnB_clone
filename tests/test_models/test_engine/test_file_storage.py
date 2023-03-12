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

    def setUp(self) -> None:
        """Run before each class test method"""
        """Before class tests runt"""
        storage.__file_path = "test.json"
        storage.__objects = {}
        self.obj = BaseModel()

    def tearDown(self) -> None:
        """Run after each class test methon"""
        del self.obj
        if pl.Path('test.json').exists():
            os.remove('test.json')

    def test_file_exist(self):
        """."""
        self.obj.save()

        self.assertTrue(pl.Path("test.json").exists())
        self.assertTrue(pl.Path("test.json").is_file())

    def test_file_storage_attribute_type(self):
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_storage_new_method(self):
        """."""
        obj_1 = BaseModel()
        storage.new(obj_1)
        info = ".".join(['BaseModel', obj_1.id])
        self.assertIn(info, storage._FileStorage__objects)
        self.assertIn(info, storage.all())

    def test_reload_method(self):
        self.obj.save()
        storage.__objects = {}
        self.assertEqual(len(storage.all()), 0)
        storage.reload()
        self.assertEqual(len(storage.all()), 1)

    def test_save_method(self):
        storage.new(self.obj)
        storage.save()
        storage.__objects = {}
        storage.reload()
        info = ".".join(['BaseModel', self.obj.id])
        self.assertIn(info, storage.all())

    def test_destroy_method(self):
        self.obj.save()
        info = ".".join(['BaseModel', self.obj.id])
        storage.destroy()
        self.assertEqual({}, storage.all())
