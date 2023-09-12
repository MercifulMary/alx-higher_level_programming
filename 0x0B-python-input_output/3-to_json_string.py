#!/usr/bin/python3
"""Defines a function for converting a Python object to a JSON string."""

import json

def to_json_string(my_obj):
    """Return the JSON representation of a Python object."""
    return json.dumps(my_obj)
