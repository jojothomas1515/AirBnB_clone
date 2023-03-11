#!/usr/bin/python3
"""Tests for the Review class."""

import os
from unittest import TestCase
from models.review import Review
from models import storage
from models.base_model import BaseModel
import pathlib as pl


class TestReview(TestCase):
    """Review class and instances tests."""

    def setUp(self):
        self.r1 = Review()
        self.r2 = Review()

    def tearDown(self):
        del self.r1
        del self.r2

    def test_Review_instance(self):
        self.assertIsInstance(self.r1, Review)
        self.assertIsInstance(self.r2, Review)
        self.assertIsInstance(self.r1, BaseModel)
        self.assertIsInstance(self.r2, BaseModel)

    def test_subclassed_from_basemodel(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_object_class(self):
        self.assertNotEqual(self.r1.__class__,
                            BaseModel)
        self.assertEqual(self.r1.__class__, Review)

    def test_Review_attributes(self):
        attr = ['email', 'password', 'first_name', 'last_name']
        for val in attr:
            self.assertIn(val, Review.__dict__.keys())

    def test_Review_attr_is_string(self):
        attr = ['email', 'password', 'first_name', 'last_name']
        for val in attr:
            self.assertIsInstance(Review.__dict__[val], str)
