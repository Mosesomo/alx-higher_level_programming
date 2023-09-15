#!/usr/bin/python3
"""This module defines a class"""


class Base:
    """Representing a class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a base class
        Args:
            id: initialized to none
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
