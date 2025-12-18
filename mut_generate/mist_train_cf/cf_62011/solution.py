"""
QUESTION:
Create a function called `sort_by_binary_len` that takes a list of positive integers as input and returns a new list where the integers are sorted based on the length of their binary representations in ascending order. If two or more integers have the same binary length, they should be sorted by their decimal values.
"""

def sort_by_binary_len(arr):
    return sorted(arr, key=lambda x: (len(bin(x))-2, x))