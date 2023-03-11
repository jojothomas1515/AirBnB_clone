#!/usr/bin/python3
"""console tests module."""

import os
import pathlib as pl
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):

    def setUp(self) -> None:
        storage._FileStorage__file_path = "test2.json"
        storage._FileStorage__objects = {}

        self.m1: dict = {"id": "11343014-1023-464f-9c60-c062236ac1f4",
                         "created_at": "2023-03-10T23:45:28.418058",
                         "updated_at": "2023-03-10T23:45:28.418093",
                         "__class__": "BaseModel"}
        self.m2: dict = {"id": "f6ab3013-d5a4-47fd-8d7b-df119283196c",
                         "created_at": "2023-03-10T23:45:34.176791",
                         "updated_at": "2023-03-10T23:45:34.176814",
                         "__class__": "User"}
        self.m1: BaseModel = BaseModel(**self.m1)
        self.m2: User = User(**self.m2)
        self.m1.save()
        self.m2.save()

    def tearDown(self) -> None:
        del self.m1
        del self.m2

        if pl.Path("test2.json").is_file():
            os.remove("test2.json")

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertRegex(f.getvalue(), r"11343014-1023-464f-9c60-c062236ac1f4")
        self.assertRegex(f.getvalue(), r"f6ab3013-d5a4-47fd-8d7b-df119283196c")

    def test_show(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                    "show BaseModel 11343014-1023-464f-9c60-c062236ac1f4"
            )
        self.assertRegex(f.getvalue(), r"11343014-1023-464f-9c60-c062236ac1f4")
        self.assertRegex(f.getvalue(), "created_at")
        self.assertRegex(f.getvalue(), "updated_at")
