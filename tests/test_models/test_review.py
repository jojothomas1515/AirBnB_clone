#!/usr/bin/python3
"""Tests for review module"""
import os
import pathlib as pl
import unittest
from datetime import datetime

from models import storage
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests Cases for Review"""

    s_file = None
    s_objs = None

    @classmethod
    def setUpClass(cls) -> None:
        if pl.Path("test.json").exists():
            os.remove("test.json")
        cls.s_objs = storage._FileStorage__objects = {}
        cls.s_file = storage._FileStorage__file_path = "test.json"

    @classmethod
    def tearDownClass(cls):
        if pl.Path("test.json").exists():
            os.remove("test.json")
        del cls.s_objs
        del cls.s_file

    def setUp(self) -> None:
        self.obj = Review()

    def tearDown(self) -> None:
        del self.obj

    def test_review_attr_instance(self):
        self.assertIsInstance(self.obj, Review)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.to_dict(), dict)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertIsInstance(self.obj.place_id, str)
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(self.obj.user_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(self.obj.text, str)
        self.assertIsInstance(Review.text, str)

    def test_review_dict_keys(self):
        data = self.obj.to_dict()
        self.assertIsInstance(data, dict)
        self.assertIn('__class__', data)
        self.assertIn('id', data)
        self.assertIn('created_at', data)
        self.assertIn('updated_at', data)
        self.assertNotIn('place_id', data)
        self.assertNotIn('user_id', data)
        self.assertNotIn('text', data)

    def test_review_dict_contents(self):
        data = self.obj.to_dict()
        self.assertEqual(data['id'], self.obj.id)
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertEqual(data['created_at'], self.obj.created_at.isoformat())
        self.assertEqual(data['updated_at'], self.obj.updated_at.isoformat())
        self.assertEqual(data['__class__'], self.obj.__class__.__name__)

    def test_user_save(self):
        time_iso = self.obj.updated_at.isoformat()
        self.obj.save()
        self.assertNotEqual(time_iso, self.obj.updated_at.isoformat())
