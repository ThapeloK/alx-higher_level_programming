#!/usr/bin/python3
"""Simple class"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Getter for __position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if any(not isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        if any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def my_print(self):
        """Prints square with #"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """String method"""
        s = ""
        if self.__size == 0:
            return s
        for _ in range(self.position[1]):
            s += '\n'
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                s += " "
            for _ in range(self.__size):
                s += '#'
            s += '\n'
        return s[:-1]
