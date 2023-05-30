#!/usr/bin/python3

"""
Module 2-square
Define class square with private attributr size and validates szie
"""


class Square:
    """
    Class square definition

    Args:
        size(int): size of a sizde on square
    """

    def __init__(self, size=0):

        """
        Initializes square

        Attributes:
            __size(int): private instance attribute side of square: 0 if None
        """

        self.__size = size

        """
        Raise ValueError and TypeError
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer ")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
