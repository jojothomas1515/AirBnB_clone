#!/usr/bin/python3
"""Console module for managing model object creation and storage."""
import cmd
import os
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """Console command line class for model management."""
    prompt = "(hbnb) "

    def emptyline(self):
        """Does Nothing."""
        pass

    def do_quit(self, line):
        """Exit the command line."""
        return True

    def do_EOF(self, line):
        """Exit the command line."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
