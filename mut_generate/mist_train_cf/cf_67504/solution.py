"""
QUESTION:
Create a function named `sort_by_binary_len` that takes a list of non-negative integers as input and returns the reordered list based on the length of their binary representations in ascending order. If two or more numbers have the same binary length, they should be reordered based on their decimal values.
"""

def sort_by_binary_len(arr):
    def binary_len(n):
        return len(bin(n)) - 2

    return sorted(sorted(arr), key=binary_len)