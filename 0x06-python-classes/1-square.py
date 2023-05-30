#!/usr/bin/python3
"""
Module 1-square
Defines the size of a square as a private instance attribute
"""


class Square:

    """
    class Square definition

    Args:
        size: size of the side of a square
    """

    def __init__(self, size):

        """
        Initializes a square

        Attributes:
            size: Size of a side of a square
        """

        self.__size = size
