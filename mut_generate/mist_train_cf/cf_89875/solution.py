"""
QUESTION:
Create a function `sort_array(arr)` that takes an array containing elements of different data types and returns the array sorted in ascending order. The sorting should prioritize integer elements, which should be placed at the beginning of the array in ascending order. The remaining string elements should be filtered to exclude those containing special characters or numbers, converted to lowercase, and then sorted based on their length.
"""

import re

def sort_array(arr):
    integers = []
    strings = []

    for element in arr:
        if isinstance(element, int):
            integers.append(element)
        elif isinstance(element, str):
            if not re.search('[^a-zA-Z]', element):  # check if element contains only alphabets
                strings.append(element.lower())

    integers.sort()
    strings.sort(key=lambda x: len(x))

    return integers + strings