"""
QUESTION:
Write a function `find_max_key` that takes a dictionary `d` as input and returns the key corresponding to the maximum value. The function should assume that the dictionary contains only numeric values and that there are no duplicate maximum values. If the dictionary is empty, the function can return any value or raise an exception.
"""

def find_max_key(d):
    max_value = max(d.values())
    for key, value in d.items():
        if value == max_value:
            return key