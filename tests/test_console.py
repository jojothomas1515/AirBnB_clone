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
    """."""

    def setUp(self) -> None:
        """."""
        storage._FileStorage__file_path = "file.json"
        storage._FileStorage__objects = {}

        self.m1: BaseModel = BaseModel()
        self.m2: User = User()
        self.m1.save()
        self.m2.save()

    def tearDown(self) -> None:
        """."""
        del self.m1
        del self.m2

        if pl.Path("file.json").is_file():
            os.remove("file.json")

    def test_all(self):
        """."""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertRegex(f.getvalue(), self.m1.id)
        self.assertRegex(f.getvalue(), self.m2.id)

    def test_show(self):
        """."""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                    "show BaseModel {}".format(self.m1.id)
            )
        self.assertRegex(f.getvalue(), self.m1.id)
        self.assertRegex(f.getvalue(), "created_at")
        self.assertRegex(f.getvalue(), "updated_at")
