#!/usr/bin/python3
"""Console module for managing model object creation and storage."""
import cmd


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

    def do_quit(self, line):
        """Exit the command line."""
        exit(1)

    def do_EOF(self, line):
        """Exit the command line."""
        exit(1)

    def emptyline(self):
        """Does Nothing."""
        pass


intro = "{}\tHBNBCommand console By JOJO THOMAS and VICTORIA OLABODEH{}\n" \
        "\n{}\tW\tE\tL\tC\tO\tM\tE\n\n{}".format(TermColor.OKCYAN, TermColor.ENDC,
                                                 TermColor.HEADER, TermColor.ENDC)
HBNBCommand().cmdloop(intro=intro)
