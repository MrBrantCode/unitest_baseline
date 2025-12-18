"""
QUESTION:
Implement a function `custom_sort(s)` that takes a string `s` and returns a sorted string. The sorting should be done in two steps: first by the length of the characters (all single characters have a length of 1) and then by their ASCII value in ascending order.
"""

def custom_sort(s):
    return ''.join(sorted(s, key=lambda x: (len(x), x)))