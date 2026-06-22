#!/usr/bin/python3
"""module for is same class function """


def is_same_class(obj, a_class):
  """function that test if the object is exactly an instance of the specified class"""

  return type(obj) is a_class
