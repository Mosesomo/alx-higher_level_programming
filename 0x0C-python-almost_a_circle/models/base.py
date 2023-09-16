#!/usr/bin/python3
"""This module defines a class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the json string
            representation of list_dictionary
        """

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON string representation
            of lists_objs to a file
        """

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_string = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(json_string))
