#!/usr/bin/python3
"""Simple class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Constructor"""
        self.size = size

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
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Greater or equal"""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Greater or equal"""
        return (self.area() != other.area())

    def __lt__(self, other):
        """Greater or equal"""
        return (self.area() < other.area())

    def __le__(self, other):
        """Greater or equal"""
        return (self.area() <= other.area())

    def __gt__(self, other):
        """Greater or equal"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Greater or equal"""
        return (self.area() >= other.area())
