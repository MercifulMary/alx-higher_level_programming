#!/usr/bin/python3

"""Defines a function for checking if an object inherits from a specific class."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        True if obj is an inherited instance of a_class, otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
