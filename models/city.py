#!/usr/bin/python3
"""Module containing the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city that inherits from BaseModel."""
    state_id = ""
    name = ""
