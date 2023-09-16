#!/usr/bin/python3
"""Defines unit tests for base.py.

Unittest classes:
    TestBaseInstantiation - line 21
    TestBaseToJsonString - line 108
    TestBaseSaveToFile - line 154
    TestBaseFromJsonString - line 232
    TestBaseCreate - line 286
    TestBaseLoadFromFile - line 338
    TestBaseSaveToFileCSV - line 404
    TestBaseLoadFromFileCSV - line 482
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the Base class."""
    
    # ... (rest of the TestBaseInstantiation class)


class TestBaseToJsonString(unittest.TestCase):
    """Unit tests for testing to_json_string method of the Base class."""
    
    # ... (rest of the TestBaseToJsonString class)


class TestBaseSaveToFile(unittest.TestCase):
    """Unit tests for testing save_to_file method of the Base class."""
    
    # ... (rest of the TestBaseSaveToFile class)


class TestBaseFromJsonString(unittest.TestCase):
    """Unit tests for testing from_json_string method of the Base class."""
    
    # ... (rest of the TestBaseFromJsonString class)


class TestBaseCreate(unittest.TestCase):
    """Unit tests for testing create method of the Base class."""
    
    # ... (rest of the TestBaseCreate class)


class TestBaseLoadFromFile(unittest.TestCase):
    """Unit tests for testing load_from_file method of the Base class."""
    
    # ... (rest of the TestBaseLoadFromFile class)


class TestBaseSaveToFileCSV(unittest.TestCase):
    """Unit tests for testing save_to_file_csv method of the Base class."""
    
    # ... (rest of the TestBaseSaveToFileCSV class)


class TestBaseLoadFromFileCSV(unittest.TestCase):
    """Unit tests for testing load_from_file_csv method of the Base class."""
    
    # ... (rest of the TestBaseLoadFromFileCSV class)


if __name__ == "__main__":
    unittest.main()
