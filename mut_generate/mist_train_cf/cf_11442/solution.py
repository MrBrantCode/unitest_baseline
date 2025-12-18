"""
QUESTION:
Write a function `find_index(array, value)` that finds the index of the first occurrence of `value` in `array`. The function should return the index of the first occurrence if found, or -1 if not found. The array can contain duplicate values and both positive and negative integers.
"""

def find_index(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1