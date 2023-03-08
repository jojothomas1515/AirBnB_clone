# AIRBNB CLONE

## PART 1: AirBnB Console

# Description

## This team project is part of the ALX School Full-Stack Software Engineer program. It's the first step towards building a first full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

# Usage

## The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.

# File Storage

## The folder engine manages the serialization and deserialization of all the data, following a JSON format.

## A FileStorage class is defined in file_storage.py with methods to follow this flow: <object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>

## The init.py file contains the instantiation of the FileStorage class called storage, followed by a call to the method reload() on that instance. This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.

# Tests

## All the code is tested with the unittest module. The test for the classes are in the test_models folder.

# Authors

## Joseph Thomas Ehigie <jojothomas1515@gmail.com>
## Oluwabunmi Victoria Olabode <bhummhie97@gmail.com>
