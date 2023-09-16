#!/usr/bin/python3
# test_rectangle.py
# Brennan D Baraban <375@holbertonschool.com>

"""Defines unittests for models/rectangle.py.

Unittest classes:
    TestRectangleInstantiation - Tests for instantiating the Rectangle class.
    TestRectangleWidth - Tests for the width attribute of the Rectangle class.
    TestRectangleHeight - Tests for the height attribute of the Rectangle class.
    TestRectangleX - Tests for the x attribute of the Rectangle class.
    TestRectangleY - Tests for the y attribute of the Rectangle class.
    TestRectangleOrderOfInitialization - Tests for the order of attribute initialization.
    TestRectangleArea - Tests for the area method of the Rectangle class.
    TestRectangleUpdateArgs - Tests for updating attributes using positional arguments.
    TestRectangleUpdateKwargs - Tests for updating attributes using keyword arguments.
    TestRectangleToDictionary - Tests for the to_dictionary method of the Rectangle class.
"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for instantiating the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    # ... (other test cases here)


class TestRectangleWidth(unittest.TestCase):
    """Tests for the width attribute of the Rectangle class."""

    # ... (test cases for width attribute here)


class TestRectangleHeight(unittest.TestCase):
    """Tests for the height attribute of the Rectangle class."""

    # ... (test cases for height attribute here)


class TestRectangleX(unittest.TestCase):
    """Tests for the x attribute of the Rectangle class."""

    # ... (test cases for x attribute here)


class TestRectangleY(unittest.TestCase):
    """Tests for the y attribute of the Rectangle class."""

    # ... (test cases for y attribute here)


class TestRectangleOrderOfInitialization(unittest.TestCase):
    """Tests for the order of attribute initialization of the Rectangle class."""

    # ... (test cases for attribute order here)


class TestRectangleArea(unittest.TestCase):
    """Tests for the area method of the Rectangle class."""

    # ... (test cases for area method here)


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for updating attributes using positional arguments in the Rectangle class."""

    # ... (test cases for update_args method here)


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for updating attributes using keyword arguments in the Rectangle class."""

    # ... (test cases for update_kwargs method here)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method of the Rectangle class."""

    # ... (test cases for to_dictionary method here)
