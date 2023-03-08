#!/usr/bin/python3
"""Console module for managing model object creation and storage."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import re


class TermColor:
    """Colors for styling outputs"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class HBNBCommand(cmd.Cmd):
    """Console command line class for model management."""
    prompt = "(hbnb)"
    model_dict: dict = {"BaseModel": BaseModel,
                        "User"     : User}

    def emptyline(self):
        """Does Nothing."""
        pass

    def do_quit(self, line):
        """Exit the command line."""
        exit(1)

    def do_EOF(self, line):
        """Exit the command line."""
        exit(1)

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
         (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
 key = ".".join((line.split(" ")[0],
                                line.split(" ")[1]))
         Args:
            line: argument that command is supposed to work
         """
        # Todo:delete instance and save further implementations
        if line == "":
            print("** class name missing **")
        elif line.split(" ")[0] in self.model_dict.keys():
            if len(line.split(" ")) == 2:
                key = ".".join((line.split(" ")[0],
                                line.split(" ")[1]))
                try:
                    del storage._FileStorage__objects[key]
                    storage.save()
                except KeyError as e:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

        # storage.destroy(line)

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
                   r"(?P<id>[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}" \
                   r"-[a-z0-9]{4}-[a-z0-9]{12})?.?" \
                   r"(?P<key>[\w\d_]+)?.?" \
                   r"(?P<value>\"[^\"]+\"|[^ ]+)?"
        validator = re.compile(reg_text)
        res = validator.search(line)
        _model, _id, _key, _value = res.groups()
        if line == "":
            print("** class name missing **")
        elif _model in self.model_dict.keys():
            if _id:
                if _key:
                    if _value:
                        # Todo: implement update
                        if _key not in ["created_at", 'updated_at', "id"]:
                            print(res.groups())
                            inst = ".".join((_model,
                                             _id))
                            try:
                                obj = storage.all()[inst]
                                obj.__dict__[_key] = eval(_value)
                                storage.save()
                            except KeyError:
                                print("** no instance found **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** attribute name missing **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


banner = """
   (_)         (_)      (_)(_)(_)(_) _       (_) _       (_)      (_)(_)(_)(_) _    
   (_)         (_)       (_)        (_)      (_)(_)_     (_)       (_)        (_)   
   (_) _  _  _ (_)       (_) _  _  _(_)      (_)  (_)_   (_)       (_) _  _  _(_)   
   (_)(_)(_)(_)(_)       (_)(_)(_)(_)_       (_)    (_)_ (_)       (_)(_)(_)(_)_    
   (_)         (_)       (_)        (_)      (_)      (_)(_)       (_)        (_)   
   (_)         (_)       (_)_  _  _ (_)      (_)         (_)       (_)_  _  _ (_)   
   (_)         (_)      (_)(_)(_)(_)         (_)         (_)      (_)(_)(_)(_)      
"""
intro = "{}\t{}\n\tconsole By JOJO THOMAS and VICTORIA OLABODEH{}\n" \
        "\n{}\tW\tE\tL\tC\tO\tM\tE\n\n{}".format(TermColor.OKCYAN, banner, TermColor.ENDC,
                                                 TermColor.HEADER, TermColor.ENDC)
if __name__ == '__main__':
    HBNBCommand().cmdloop(intro=intro)
