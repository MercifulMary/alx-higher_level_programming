#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.

    Attributes:
        __slots__ (list): A list of allowed attribute names.
            Only 'first_name' is allowed for this class.
    """
    __slots__ = ["first_name"]
