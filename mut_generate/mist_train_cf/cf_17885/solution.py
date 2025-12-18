"""
QUESTION:
Write a function `print_array_without_duplicates` that takes an array of integers as input and returns the array with all duplicate elements removed. The input array can contain both positive and negative integers. You cannot use any built-in functions or data structures that can check for duplicates, such as sets or lists with built-in duplicate checking methods.
"""

def print_array_without_duplicates(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result