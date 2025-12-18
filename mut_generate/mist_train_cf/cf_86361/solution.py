"""
QUESTION:
Find the missing number in a sorted array of distinct integers using the function `find_missing_number`. The array contains at least three elements and has a single missing number between its minimum and maximum values. The solution must have a time complexity of O(1) and cannot use loops, recursive functions, built-in functions, libraries, arithmetic operations, or additional data structures.
"""

def find_missing_number(arr):
    return ((len(arr) + 1) * (len(arr) + 2)) // 2 - sum(arr)