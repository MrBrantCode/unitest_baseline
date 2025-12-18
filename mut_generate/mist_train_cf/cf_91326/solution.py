"""
QUESTION:
Write a function named `is_palindrome` that takes a one-dimensional array of integers and/or floating point numbers as input and returns `True` if the array is a palindrome and `False` otherwise. The function should handle arrays containing negative integers and consider the order and type of elements.
"""

def is_palindrome(arr):
    reversed_arr = arr[::-1]
    return arr == reversed_arr