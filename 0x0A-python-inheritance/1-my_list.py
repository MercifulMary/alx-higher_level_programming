#!/usr/bin/python3

"""Defines a custom list class MyList that inherits from the built-in list class."""


class MyList(list):
    """Implements a method for printing the list in sorted ascending order."""

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))
