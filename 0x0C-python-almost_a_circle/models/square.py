#!/usr/bin/python3
"""This mofule defines a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class square that inherits from class
    Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing class square
        Args:
            size: size of the square
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of a square"""

        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.height))
