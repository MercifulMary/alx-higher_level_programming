#!/usr/bin/python3

"""Defines a base geometry class called BaseGeometry."""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """This method is not implemented and should be overridden in subclasses."""
        raise Exception("area() is not implemented")
