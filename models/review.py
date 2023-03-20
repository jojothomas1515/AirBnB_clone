#!/usr/bin/python3
"""Review class module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for review instances."""

    place_id: str = ""
    user_id: str = ""
    text: str = ""
