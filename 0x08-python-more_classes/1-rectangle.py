#!/usr/bin/python3
"""
Modeule 1-rectangle
contains class Rectangle
with private width and height attributes
"""


class Rectangle:
    """
    Defines class rectangle with private height and width attributes

    Args:
        width(int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """Initialize rectangles"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must ne an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter retrieves height """
        return self._height

    @height.setter
    def height(self, value):
        """ Setter sets the height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
