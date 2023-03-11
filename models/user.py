#!/usr/bin/python3
"""User Model Subclassed from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for user object instantiation.

    Args:
        email (str): The user's email.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
