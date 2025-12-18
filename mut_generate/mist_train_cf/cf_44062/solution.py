"""
QUESTION:
Write a function named `next_palindrome(n)` that takes an integer `n` as input and returns the smallest palindrome number greater than `n`.
"""

def next_palindrome(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    
    n += 1
    while not is_palindrome(n):
        n += 1
    return n