"""
QUESTION:
Create a function called `is_palindrome` that determines if a given integer is a palindrome, considering both positive and negative numbers. The function should be able to handle large numbers efficiently without converting them to strings. The function should return a boolean value indicating whether the number is a palindrome or not.
"""

def entance(num):
    # Handle negative numbers
    if num < 0:
        num = -num

    original_num = num
    reversed_num = 0

    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num //= 10

    return original_num == reversed_num