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
        self.size = size

    @property
    def size(self):
        """
        Get/set the current size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
