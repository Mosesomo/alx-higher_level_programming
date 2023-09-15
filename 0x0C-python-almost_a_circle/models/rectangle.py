#!/usr/bin/python3
"""This module defines a class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Representing a class rectangle that inherits from
        base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class rectangle
        Args:
            width: width size of the rectangle
            height: height size of the rectangle
            x: argument
            y: argument
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
