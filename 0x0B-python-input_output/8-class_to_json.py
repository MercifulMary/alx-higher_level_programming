#!/usr/bin/python3
"""Defines a function for converting a Python class instance to a JSON dictionary."""
  
def class_to_json(obj):
    """Return the dictionary representation of a Python class instance."""
    return obj.__dict__
