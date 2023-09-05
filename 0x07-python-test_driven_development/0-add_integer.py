#!/usr/bin/python3
# 0-add_integer.py
"""Defines a function for adding two integers or floats."""

def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added.
    
    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
