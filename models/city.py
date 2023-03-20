#!/usr/bin/python3
"""city model module."""
from models.base_model import BaseModel


class City(BaseModel):
    """city class for city instance."""

    state_id: str = ""
    name: str = ""
