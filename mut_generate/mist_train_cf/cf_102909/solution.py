"""
QUESTION:
Write a function `is_palindrome` that takes an array of integers or floating point numbers as input and returns `True` if the array is a palindrome (remains the same when reversed), and `False` otherwise. The function should handle arrays containing negative integers and floating point numbers and consider the order and type of elements. The input array is one-dimensional.
"""

def is_palindrome(arr):
    reversed_arr = arr[::-1]
    return arr == reversed_arr