#!/usr/bin/python3
"""init module that makes the directory a package"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
