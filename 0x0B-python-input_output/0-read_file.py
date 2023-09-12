#!/usr/bin/python3
"""Defines a function for reading and printing the contents of a text file."""

def read_file(filename=""):
    """
    Print the contents of a UTF-8 text file to stdout.

    Args:
        filename (str): The name of the text file to be read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
