"""
QUESTION:
Create a recursive function named `sumDigits` that takes an integer as input and returns the sum of its digits. The function should not use any built-in functions for converting numbers to strings or vice versa. Then, calculate the remainder when this sum is divided by 9.
"""

def sumDigits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sumDigits(num // 10)