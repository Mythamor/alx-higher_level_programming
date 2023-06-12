#!usr/bin/python3
"""
Module 1-my_list

Contains class MyList
inherits from list; has public instance method to print sorted
"""


class MyList(list):
    """
    Inherits from list

    methods:
    print_sorted(self):
    """
    def print_sorted(self):
        """
        prints list of ints in sorted ASC order
        """
        print(sorted(self))
