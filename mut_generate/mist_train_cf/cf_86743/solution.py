"""
QUESTION:
Implement a function named `sort_2d_list` to sort a 2-dimensional list in ascending order based on the first element of each sublist when it's a datetime object, and the second element when it's not a datetime object. The function should handle the second element being a string, negative number, float, or tuple, with a time complexity of O(n log n), without using built-in Python sorting functions.
"""

from datetime import datetime

def sort_2d_list(lst):
    def key_function(item):
        if isinstance(item[0], datetime):
            return (0, item[0])
        elif isinstance(item[1], str):
            return (1, item[1])
        elif isinstance(item[1], int):
            return (2, item[1])
        elif isinstance(item[1], float):
            return (3, item[1])
        elif isinstance(item[1], tuple):
            return (4, item[1])
        else:
            return (5, item[1])

    return sorted(lst, key=key_function)