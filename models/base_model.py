#!/usr/bin/python3
"""
Base Model module.

Define all common attributes and methods of other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base Model abstract class."""

    def __init__(self, *args, **kwargs):
        """Basemodel constructor.

        Args:
            id: string - assign with an uuid when an instance is created.
            created_at: datetime - assign with the current datetime when an instance is created.
            updated_at: datetime - assign with the current datetime when an instance is created
            and it will be updated every time you change.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """Update instance attributes and write the timestamp to the updated_at attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dicttionary representation of instance attributes."""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

    def __str__(self) -> str:
        """Readable representation of the class."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)


if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key,
              type(my_model_json[key]), my_model_json[key]))
