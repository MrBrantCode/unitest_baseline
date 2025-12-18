"""
QUESTION:
Write a function called `is_palindrome(n)` that takes an integer `n` as input and returns `True` if the number is a palindrome and `False` otherwise. The function should not use any additional data structures or variables beyond the input `n`.
"""

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]