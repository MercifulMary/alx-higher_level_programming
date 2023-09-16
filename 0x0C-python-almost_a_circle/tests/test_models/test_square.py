#!/usr/bin/python3
# test_square.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines unittests for models/square.py.

Unittest classes:
    TestSquareInstantiation - line 24
    TestSquareSize - line 88
    TestSquareX - line 166
    TestSquareY - line 238
    TestSquareOrderOfInitialization - line 306
    TestSquareArea - line 322
    TestSquareStdout - line 343
    TestSquareUpdateArgs - line 426
    TestSquareUpdateKwargs - line 538
    TestSquareToDictionary - 640
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    # ... (rest of the existing code)

class TestSquareSize(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    # ... (rest of the existing code)

class TestSquareX(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    # ... (rest of the existing code)

class TestSquareY(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    # ... (rest of the existing code)

class TestSquareOrderOfInitialization(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""

    # ... (rest of the existing code)

class TestSquareArea(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    # ... (rest of the existing code)

class TestSquareStdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""

    # ... (rest of the existing code)

class TestSquareUpdateArgs(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    # ... (rest of the existing code)

class TestSquareUpdateKwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""

    # ... (rest of the existing code)

class TestSquareToDictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    # ... (rest of the existing code)


if __name__ == "__main__":
    unittest.main()
