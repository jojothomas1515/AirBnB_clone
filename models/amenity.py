#!/usr/bin/python3
"""Amenities Module."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class for creating instances."""
    name: str = ""
