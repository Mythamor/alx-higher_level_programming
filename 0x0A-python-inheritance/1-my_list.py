#!/usr/bin/python3
"""
Module 1-my_list
"""


class MyList(list):
    """class that inherits from list
        
        Methods:
        print_sorted(self)
    """


    def print_sorted(self):
        """ print sorted list"""
        print(sorted(self))
