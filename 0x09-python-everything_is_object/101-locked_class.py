#!/usr/bin/python3
"""A locked class
"""


class LockedClass:
    """
    A class LockedClass with no class or object attribute, that prevents 
    the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        self.first_name = first_name
