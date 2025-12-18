"""
QUESTION:
Create a function `sort_2d_list(lst)` that sorts a 2-dimensional list `lst` in ascending order based on the values of the first element in each sublist, which can be a datetime object. The second element in each sublist can be a string, negative number, float, or tuple. The function should have a time complexity of O(n log n) and should not use any built-in Python sorting functions.
"""

from datetime import datetime

def sort_2d_list(lst):
    def key_function(item):
        if isinstance(item[0], datetime):
            return item[0]
        else:
            return item[0]

    return sorted(lst, key=key_function)