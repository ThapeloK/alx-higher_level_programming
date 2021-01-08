#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """a: integer or float
    b: integer or float
    Return: The sum of a and b"""

    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
