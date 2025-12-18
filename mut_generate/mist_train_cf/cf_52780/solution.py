"""
QUESTION:
Create a function called `sort_dicts` that sorts an array of dictionaries by two keys, "name" and "age". The function should first sort the array by the "name" key and then by the "age" key in case of a tie. The function should return the sorted array.
"""

import operator

def sort_dicts(arr):
    arr.sort(key=operator.itemgetter('name', 'age'))
    return arr