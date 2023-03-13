#!/usr/bin/python3
"""Tests for place module"""
import os
import pathlib as pl
import unittest
from datetime import datetime

from models import storage
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests Cases for Place"""

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
        self.obj = Place()

    def tearDown(self) -> None:
        del self.obj

    def test_place_attr_instance(self):
        self.assertIsInstance(self.obj, Place)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.to_dict(), dict)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertIsInstance(self.obj.name, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(self.obj.city_id, str)
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(self.obj.user_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(self.obj.description, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(self.obj.number_rooms, int)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(self.obj.number_bathrooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(self.obj.max_guest, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(self.obj.price_by_night, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(self.obj.latitude, float)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(self.obj.longitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(self.obj.amenity_ids, list)
        self.assertIsInstance(Place.amenity_ids, list)

    def test_place_dict_keys(self):
        data = self.obj.to_dict()
        self.assertIsInstance(data, dict)
        self.assertIn('__class__', data)
        self.assertIn('id', data)
        self.assertIn('created_at', data)
        self.assertIn('updated_at', data)
        self.assertNotIn('city_id', data)
        self.assertNotIn('user_id', data)
        self.assertNotIn('name', data)
        self.assertNotIn('description', data)
        self.assertNotIn('number_rooms', data)
        self.assertNotIn('number_bathrooms', data)
        self.assertNotIn('max_guest', data)
        self.assertNotIn('price_by_night', data)
        self.assertNotIn('latitude', data)
        self.assertNotIn('longitude', data)
        self.assertNotIn('amenity_ids', data)

    def test_place_dict_contents(self):
        data = self.obj.to_dict()
        self.assertEquals(data['id'], self.obj.id)
        self.assertEquals(Place.name, "")
        self.assertEquals(Place.city_id, "")
        self.assertEquals(Place.user_id, "")
        self.assertEquals(Place.description, "")
        self.assertEquals(Place.number_rooms, 0)
        self.assertEquals(Place.number_bathrooms, 0)
        self.assertEquals(Place.max_guest, 0)
        self.assertEquals(Place.price_by_night, 0)
        self.assertEquals(Place.latitude, 0.0)
        self.assertEquals(Place.longitude, 0.0)
        self.assertEquals(Place.amenity_ids, [])
        self.assertEquals(data['created_at'], self.obj.created_at.isoformat())
        self.assertEquals(data['updated_at'], self.obj.updated_at.isoformat())
        self.assertEquals(data['__class__'], self.obj.__class__.__name__)

    def test_user_save(self):
        time_iso = self.obj.updated_at.isoformat()
        self.obj.save()
        self.assertNotEqual(time_iso, self.obj.updated_at.isoformat())
