#!/usr/bin/python3
"""Defines a square printing function"""


def print_square(size):
    """Print_square
    Args: size is the size
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    size = int(size)
    print(("#" * size + '\n') * size, end="")
