#!/usr/bin/python3
"""A Python program on Classes"""

class Square:
    """Represents a class that defines a square
    Private instance attribute: size
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
