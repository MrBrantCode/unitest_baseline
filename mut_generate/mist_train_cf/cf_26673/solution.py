"""
QUESTION:
Write a function `is_palindrome(x)` that takes a non-negative integer `x` as input and returns a boolean indicating whether `x` is a palindrome. The function should not convert the integer to a string. A palindrome is a number that reads the same backward as forward.
"""

def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False  
    reversed_num = 0
    original_num = x
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return original_num == reversed_num