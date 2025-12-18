"""
QUESTION:
Write a function `print_array_without_duplicates(arr)` that prints an array of integers without duplicate elements, given that the input array `arr` contains a mix of positive and negative integers, and that no built-in functions or data structures other than lists can be used.
"""

def print_array_without_duplicates(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result