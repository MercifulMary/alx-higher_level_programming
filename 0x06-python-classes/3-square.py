#!/usr/bin/python3
"""
This script defines a class Square that represents a square object.
"""

class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square's sides.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides (default is 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
