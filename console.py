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
    model_dict: dict = {"BaseModel": BaseModel,
                        "User": User,
                        "Place": Place,
                        "State": State,
                        "City": City,
                        "Amenity": Amenity,
                        "Review": Review}

    def emptyline(self):
        """Does Nothing."""
        pass

    def do_quit(self, line):
        """Exit the command line."""
        return True

    def do_EOF(self, line):
        """Exit the command line."""
        return True

    def all(self, line):
        """all method up be called by default,
        parses the regex and run if it matches.
        """
        my_re = r"({})?\.?(all\(\))?".format(
                "|".join(self.model_dict.keys())
        )
        regex = re.compile(my_re)
        model, cond = regex.search(line).groups()
        if not cond:
            return False
        if cond and model in self.model_dict.keys():
            result = storage.all()
            for k, v in result.items():
                if k.split(".")[0] == model:
                    print(v)
            return True
        else:
            print("** class doesn't exist **")
            return True

    def count(self, line):
        """count method up be called by default,
        parses the regex and run if it matches.
        """
        li = []
        my_re = r"(?P<model>{})?\.?(?P<command>count\(\))?".format(
                "|".join(self.model_dict.keys())
        )
        regex = re.compile(my_re)
        model, cond = regex.search(line).groups()
        if not cond:
            return False
        if cond and model in self.model_dict.keys():
            result = storage.all()
            for k, v in result.items():
                if k.split(".")[0] == model:
                    li.append(v)
            print(li.__len__())
            return True
        else:
            print("** class doesn't exist **")
            return True

    def show(self, line):
        """show method up be called by default,
        parses the regex and run if it matches.
        """
        my_re = r"(?P<model>{})?\.?" \
                r"(?P<command>show\((?P<id>\"[^\"]+\")?\))?".format(
                "|".join(self.model_dict.keys()))
        regex = re.compile(my_re)
        model, cond, r_id = regex.search(line).groups()
        if cond:
            if not r_id:
                print("** id is missing **")
                print("** Usage <Model>.show(\"<id>\") **")
                return True
        else:
            return False
        if cond and model in self.model_dict.keys():
            result = storage.all()
            key = ".".join((model, eval(r_id)))
            try:
                print(result[key])
            except KeyError:
                print("** no instance found **")
            return True
        else:
            print("** class doesn't exist **")
            return True

    def destroy(self, line):
        """destroy method up be called by default,
                parses the regex and run if it matches.
        """
        my_re = r"(?P<model>{})?\.?" \
                r"(?P<command>destroy\((?P<id>\"[^\"]+\")?\))?".format(
                "|".join(self.model_dict.keys()))
        regex = re.compile(my_re)
        model, cond, r_id = regex.search(line).groups()
        if cond:
            if not r_id:
                print("** id is missing **")
                print("** Usage <Model>.destroy(\"<id>\") **")
                return True
        else:
            return False
        if cond and model in self.model_dict.keys():
            key = ".".join((model, eval(r_id)))
            if storage.destroy(key):
                return True
            else:
                print("** no instance found **")
                return True
        else:
            print("** class doesn't exist **")
            return True

    def update(self, line):
        """update method up be called by default,
         parses the regex and run if it matches.
        """
        my_re = r"(?P<model>{})?\.?".format(
                "|".join(self.model_dict.keys())) + \
                r"(?P<command>update\((?P<id>\"[^\"]+\")?,?\s?" \
                r"(?P<key>\"[^\"]+\"|\{[^\}]+\})?,?\s?" \
                r"(?P<value>\"?[^\"]+\"?)?\)" \
                r")?"

        regex = re.compile(my_re)
        model, cond, r_id, r_key, r_value = regex.search(line).groups()
        if cond:
            if not r_id:
                print("** id is missing **")
                print("** Usage <Model>.update(\"<id>\") **")
                return True
        else:
            return False

        if cond and model in self.model_dict.keys():
            obj_key = ".".join((model, eval(r_id)))
            try:
                obj: object = storage.all()[obj_key]
                r_key = eval(r_key)
                if isinstance(r_key, dict):
                    if "id" in r_key:
                        del r_key["id"]
                    if "__class__" in r_key:
                        del r_key["__class__"]
                    obj.__dict__.update(r_key)
                else:
                    if r_key not in ['id', '__class__']:
                        obj.__dict__[r_key] = eval(r_value)
                    else:
                        print("** cant update id or add __class__ key to dict **")
                storage.save()
            except (KeyError, AttributeError):
                print("** no instance found **")
        else:
            print("** class doesn't exist **")
            return True
        return (True)

    def do_clear(self, line):
        """Clear the terminal window."""
        os.system("clear")

    def default(self, line: str) -> None:
        """Using regular expression to map command
        Args:
            line (str): command from the stdin
        """
        if self.all(line):
            pass
        elif self.count(line):
            pass
        elif self.show(line):
            pass
        elif self.destroy(line):
            pass
        elif self.update(line):
            pass
        else:
            print("** invalid command **")

    def do_create(self, line: str):
        """Create a new instance of BaseModel.
        Args:
            line: argument that command is supposed to work
        """

        if line == "":
            print("** class name missing **")
        elif line in self.model_dict.keys():
            obj = self.model_dict[line]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.

        Args:
            line: argument that command is supposed to work
        """

        if line == "":
            print("** class name missing **")
        elif line.split(" ")[0] in self.model_dict.keys():
            if len(line.split(" ")) == 2:
                result = storage.all()
                key = ".".join((line.split(" ")[0],
                                line.split(" ")[1]))
                if key in result.keys():
                    print(result[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
         (save the change into the JSON file).
         Ex: $ destroy BaseModel 1234-1234-1234.
         key = ".".join((line.split(" ")[0],
         line.split(" ")[1]))
         Args:
            line: argument that command is supposed to work
         """
        if line == "":
            print("** class name missing **")
        elif line.split(" ")[0] in self.model_dict.keys():
            if len(line.split(" ")) == 2:
                key = ".".join((line.split(" ")[0],
                                line.split(" ")[1]))
                if storage.destroy(key):
                    pass
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name.
        Ex: $ all BaseModel or $ all.

        Args:
            line: command argument
        """
        result: dict
        if line == "":
            result = storage.all()
            for key, value in result.items():
                print(value)
        elif line in self.model_dict.keys():
            result = storage.all()
            for k, v in result.items():
                if k.split(".")[0] == line:
                    print(v)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).

        Example:
            update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Args:
            line: command argument
        """
        reg_text = r"(?P<model>{})?.?" \
                       .format("|".join(self.model_dict.keys())) + \
                   r"(?P<id>\"?[^\"]+\"?)?.?" \
                   r"(?P<key>[\w\d_]+)?.?" \
                   r"(?P<value>\"[^\"]+\"|[^ ]+)?"
        validator = re.compile(reg_text)
        res = validator.search(line)
        _model, _id, _key, _value = res.groups()
        if line == "":
            print("** class name missing **")
        elif _model in self.model_dict.keys():
            if _id:
                inst = ".".join((_model,
                                 _id))
                try:
                    obj = storage.all()[inst]
                    if _key:
                        if _value:
                            if _key not in ["created_at", 'updated_at', "id"]:
                                obj.__dict__[_key] = eval(_value)
                                storage.save()

                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                except AttributeError:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
