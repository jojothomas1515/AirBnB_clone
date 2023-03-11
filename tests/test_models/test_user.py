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
