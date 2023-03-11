#!/usr/bin/python3
"""Tests for the user class."""

import os
from unittest import TestCase
from models.user import User
from models import storage
from models.base_model import BaseModel
import pathlib as pl


class TestUser(TestCase):
    """User class and instances tests."""

    def setUp(self):
        self.u1 = User()
        self.u2 = User()

    def tearDown(self):
        del self.u1
        del self.u2

    def test_user_instance(self):
        self.assertIsInstance(self.u1, User)
        self.assertIsInstance(self.u2, User)
        self.assertIsInstance(self.u1, BaseModel)
        self.assertIsInstance(self.u2, BaseModel)

    def test_subclassed_from_basemodel(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_object_class(self):
        self.assertNotEqual(self.u1.__class__,
                            BaseModel)
        self.assertEqual(self.u1.__class__, User)

    def test_user_attributes(self):
        attr = ['email', 'password', 'first_name', 'last_name']
        for val in attr:
            self.assertIn(val, User.__dict__.keys())

    def test_user_attr_is_string(self):
        attr = ['email', 'password', 'first_name', 'last_name']
        for val in attr:
            self.assertIsInstance(User.__dict__[val], str)


class TestUserAndFileStorage(TestCase):
    """User and FileStorage Tests."""

    def setUp(self):
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
        del self.u1
        del self.u2

        if pl.Path("test.json").is_file():
            os.remove("test.json")
