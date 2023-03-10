#!/usr/bin/python3
"""File storage engine module."""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serialize data and save it as json, also deserialize
    json and create objects.

    Args:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects
        by <class name>.id (ex: to store a BaseModel object with id=12121212,
        the key will be BaseModel.12121212).
    """
    __file_path: str = "file.json"
    __objects: dict = dict()

    def all(self):
        """Returns the dictionary objects <__objects>."""

        return self.__objects

    def new(self, obj):
        """ Set in the object in the __object dictionary with the kay
        which is a combination of the object class and the id
        example BaseModel.121212
        obj: instance object to serialize
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize and save the object to a json file
        specified by __file_path
        """
        temp_dictionary: dict = {k: v.to_dict() for k, v in
                                 self.__objects.items()}
        # for k, v in self.__objects.items():
        #     try:
        #         temp_dictionary[k] = v.to_dict()
        #     except AttributeError as e:
        #         temp_dictionary[k] = v

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(temp_dictionary, f)

    def destroy(self, key):
        try:
            del self.__objects[key]

            self.save()
            return True
        except KeyError:
            return False

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised).
        """

        __model_classes = {"BaseModel": BaseModel,
                           "User"     : User,
                           "Place"    : Place,
                           "State"    : State,
                           "City"     : City,
                           "Amenity"  : Amenity,
                           "Review"   : Review}
        temp_dict: dict = {}
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                temp_dict = json.loads(f.read())
            for key, value in temp_dict.items():
                s_key = key.split(".")[0]
                if s_key in __model_classes.keys():
                    self.__objects[key] = __model_classes[s_key](**value)
        except (KeyError, FileNotFoundError):
            pass
