#!/usr/bin/python3
"""A program on Classes"""


class Square:
    """Represents a square
    Private instance attribute: size
    Instantiation with optional size
    Public instance method: def area(self)
    """

    def __init__(self, size=0):
        """Initializes the data"""
        self.__size = size

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @property.setter
    def size(self, value):
        """Sets it"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
