"""
QUESTION:
Create a function named `is_palindrome` that determines whether a given integer is a palindrome or not. The function should be able to handle negative numbers and large numbers efficiently without converting them to strings.
"""

def is_palindrome(x):
    if x < 0:
        x = -x

    original_num = x
    reversed_num = 0

    while x > 0:
        reversed_num = (reversed_num * 10) + (x % 10)
        x //= 10

    return original_num == reversed_num