#!usr/bin/python3
"""This module contains a base class for all models"""


class Base:
    """Defines a base class for all models"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            # Increment the count of objects and assign an ID
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
