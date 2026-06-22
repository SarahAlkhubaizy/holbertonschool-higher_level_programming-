#!/usr/bin/python3
"""Module for kind of class function"""


def is_kind_of_class(obj, a_class):
    """function return true if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class"""
    return isinstance(obj,a_class)
