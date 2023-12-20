#!/usr/bin/python3
"""shebang line"""


class Square:
    """A class that represent a square"""
    def __init__(self, size=0):
        """
            Initializes a new square.
            Parameters:
                size (int): side length. Default is 0.
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
