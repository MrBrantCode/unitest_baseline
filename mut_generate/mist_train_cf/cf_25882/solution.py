"""
QUESTION:
Write a function `next_palindrome(n)` that takes an integer `n` and returns the smallest palindrome number greater than `n`.
"""

def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(num):
    return str(num) == str(num)[::-1]