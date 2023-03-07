#!/usr/bin/python3
"""File storage engine module."""
import json


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

        temp_dict: dict = {}
        # k: stands for key and v: stands for value
        for k, v in self.__objects.items():
            try:
                temp_dict[k] = v.to_dict()
            except Exception as e:
                temp_dict[k] = v
        return temp_dict

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
        temp_dictionary: dict = {}
        for k, v in self.__objects.items():
            try:
                temp_dictionary[k] = v.to_dict()
            except AttributeError as e:
                temp_dictionary[k] = v

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(temp_dictionary, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised).
        """

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                self.__objects = json.loads(f.read())
        except Exception:
            pass
