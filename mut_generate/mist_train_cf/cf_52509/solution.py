"""
QUESTION:
Write a function called `alphanumeric_sort` that takes a list of strings as input, where each string can contain a combination of numeric and alphabetic characters. The function should return the smallest alphanumeric sequence from the list, considering digits first, then uppercase letters, and then lowercase letters. The input list can contain a mix of isolated numbers, single word items, and complex combinations of both numbers and letters.
"""

import re

def alphanumeric_sort(array):
    # Uses built-in sort function with special sorting key
    array.sort(key=lambda item: [(int(part) if part.isdigit() else part) for part in re.split('([0-9]+)', item)])
    return array[0]