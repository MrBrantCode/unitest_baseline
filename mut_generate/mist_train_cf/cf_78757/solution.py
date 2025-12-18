"""
QUESTION:
Write a function `is_palindrome` that takes an integer `num` as input and returns `True` if the number is a palindrome and `False` otherwise. The function should be efficient in terms of memory and computation time to handle large numbers.
"""

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]