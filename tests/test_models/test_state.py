#!/usr/bin/python3
"""Tests for state module"""
import os
import pathlib as pl
import unittest
from datetime import datetime

from models import storage
from models.state import State


class TestState(unittest.TestCase):
    """Tests Cases for State"""

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
        self.obj = State()

    def tearDown(self) -> None:
        del self.obj

    def test_state_attr_instance(self):
        self.assertIsInstance(self.obj, State)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.to_dict(), dict)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertIsInstance(self.obj.name, str)
        self.assertIsInstance(State.name, str)

    def test_state_dict_keys(self):
        data = self.obj.to_dict()
        self.assertIsInstance(data, dict)
        self.assertIn('__class__', data)
        self.assertIn('id', data)
        self.assertIn('created_at', data)
        self.assertIn('updated_at', data)
        self.assertNotIn('name', data)

    def test_state_dict_contents(self):
        data = self.obj.to_dict()
        self.assertEqual(data['id'], self.obj.id)
        self.assertEqual(State.name, "")
        self.assertEqual(data['created_at'], self.obj.created_at.isoformat())
        self.assertEqual(data['updated_at'], self.obj.updated_at.isoformat())
        self.assertEqual(data['__class__'], self.obj.__class__.__name__)

    def test_user_save(self):
        time_iso = self.obj.updated_at.isoformat()
        self.obj.save()
        self.assertNotEqual(time_iso, self.obj.updated_at.isoformat())
