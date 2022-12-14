#!/usr/bin/python3
"""
Defines a rectangle
"""


class Rectangle:
    """
    Represents a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the data
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the data"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.property
    def height(self):
        """Retrieves the data"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
