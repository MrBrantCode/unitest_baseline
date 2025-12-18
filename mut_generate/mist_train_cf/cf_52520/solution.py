"""
QUESTION:
Construct a function `sort_by_binary_len` that takes a list of exclusively positive integers as input and returns a new list with the integers reordered in ascending order based on the length of their binary representations. In cases where multiple integers have the same binary length, the sorting should be done based on their decimal values.
"""

def sort_by_binary_len(arr):
    return sorted(arr, key=lambda x: (len(bin(x))-2, x))