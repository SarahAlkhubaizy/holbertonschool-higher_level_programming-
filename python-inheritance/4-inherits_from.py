#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """return object is an instance of a class that inherited """
    return isinstance(obj, a_class) and type(obj) is not a_class
