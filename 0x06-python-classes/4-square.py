#!/usr/bin/python3
"""Simple class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Constructor"""
        #self.size = size
        self.size(size)

    def area(self):
        """Area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter function for __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function for __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
