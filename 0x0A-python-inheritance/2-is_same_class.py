#!/usr/bin/python3

"""Defines a function for checking if an object is an instance of a specific class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
