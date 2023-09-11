#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """This method is not implemented and should be overridden in subclasses."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter value.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle.

        Returns:
            str: A string in the format [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Represents a square using Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square.

        Returns:
            str: A string in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__width}/{self.__height}"
