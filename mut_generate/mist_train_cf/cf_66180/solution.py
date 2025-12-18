"""
QUESTION:
Write a function `is_palindrome(n)` that checks if a given positive integer `n` is a palindrome without using any built-in string manipulation functions. Additionally, create a function `is_square_palindrome(n)` that determines if the square of `n` is a palindrome by utilizing the `is_palindrome(n)` function. Both functions should only work with positive integers.
"""

def is_palindrome(n):
    original_num = n
    reverse_num = 0

    while n > 0:
        digit = n % 10
        reverse_num = reverse_num * 10 + digit
        n = n // 10

    return original_num == reverse_num


def is_square_palindrome(n):
    square = n * n
    return is_palindrome(square)