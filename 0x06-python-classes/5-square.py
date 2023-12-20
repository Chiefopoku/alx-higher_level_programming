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
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            for j in range (self.__size):
                print("#", end="")
        print("")

        if self.__size == 0:
            print("")
