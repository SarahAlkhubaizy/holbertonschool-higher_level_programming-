#!/usr/bin/python3
"""Module for kind of class function."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or its subclasses."""
    return isinstance(obj, a_class)
