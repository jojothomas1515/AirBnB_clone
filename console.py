#!/usr/bin/python3
"""Console module for managing model object creation and storage."""
import cmd
from models.base_model import BaseModel
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
    model_dict: dict = {"BaseModel": BaseModel}

    # validator = re.compile(r"([A-Z][^\.]+)\.([\w-]+)")

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
            obj = self.model_dict[line]().save()
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
        elif line.split(".")[0] in self.model_dict.keys():
            if len(line.split(".")) == 2:
                result = storage.all()
                if line in result.keys():
                    print(result[line])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
         (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.

         Args:
            line: argument that command is supposed to work
         """
        # Todo:delete instance and save further implementations
        if line == "":
            print("** class name missing **")
        elif line.split(".")[0] in self.model_dict.keys():
            if len(line.split(".")) == 2:
                try:
                    del storage._FileStorage__objects[line]
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
        """
        result: dict
        if line == "":
            result = storage.all()
            for k, v in result.items():
                print(BaseModel(**v))
        elif line in self.model_dict.keys():
            result = storage.all()
            for k,v in result.items():
                if k.split(".")[0] == line:
                    print(BaseModel(**v))
        else:
            print("** class doesn't exist **")


def emptyline(self):
    """Does Nothing."""
    pass

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
        "\n{}\tW\tE\tL\tC\tO\tM\tE\n\n{}".format(TermColor.OKCYAN,banner,TermColor.ENDC,
                                                 TermColor.HEADER, TermColor.ENDC)

if __name__ == '__main__':
    HBNBCommand().cmdloop(intro=intro)
