#!/usr/bin/python3
"""A Python program on Classes"""

class Square:
    """Represents a square
    Private instance attribute: size
    Instantiation with optional size
    Public instance method that returns the current square area.
    """

    def __init__(self, size=0):
        """Initialises the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns current square area."""
        return self.__size ** 2
