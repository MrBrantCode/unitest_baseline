"""
QUESTION:
Create a function named `find_insertion_point` that takes three parameters: a sorted list `lst`, a value to be inserted, and an optional boolean parameter `reverse` with a default value of `False`. The function should return the index where the value can be inserted to maintain the sorted order of the list. The function should support lists with various data types (integers, floats, strings, tuples) and both ascending and descending orders.
"""

import bisect

def find_insertion_point(lst, value, reverse=False):
    if reverse:
        lst = lst[::-1]
    i = bisect.bisect_left(lst, value)
    if reverse:
        return len(lst) - i
    return i