#!/usr/bin/python3
"""Test for Basemodel"""
import os
import unittest

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
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
        """."""
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_storage_new_method(self):
        """."""
        u1 = User()
        s1 = State()
        c1 = City()
        a1 = Amenity()
        p1 = Place()
        r1 = Review()

        objs = [self.obj, u1, s1, c1, a1, p1, r1]

        self.assertEqual(len(storage.all()), 7)

        i = 0
        for key, val in storage.all().items():
            obj_key = "{}.{}".format(objs[i].__class__.__name__, objs[i].id)
            self.assertEqual(obj_key, key)
            self.assertTrue(val is objs[i])
            i += 1

    def test_reload_method(self):
        """."""
        self.obj.save()
        storage.__objects = {}
        self.assertEqual(len(storage.all()), 0)
        storage.reload()
        self.assertEqual(len(storage.all()), 1)

    def test_save_method(self):
        """."""
        storage.save()
        storage.__objects = {}
        storage.reload()
        info = ".".join(['BaseModel', self.obj.id])
        self.assertIn(info, storage.all())

    def test_destroy_method(self):
        """."""
        self.obj.save()
        info = ".".join(['BaseModel', self.obj.id])
        storage.destroy(info)
        self.assertEqual({}, storage.all())

    def test_storage_new_more_args(self):
        """ Test the new method with more args """

        with self.assertRaises(TypeError):
            storage.new("b1", "u1")

    def test_storage_new_less_args(self):
        """ Test the new method with less args """

        with self.assertRaises(TypeError):
            storage.new()
