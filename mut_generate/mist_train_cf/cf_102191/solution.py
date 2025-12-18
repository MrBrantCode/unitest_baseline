"""
QUESTION:
Define a recursive function `sumDigits` that takes an integer `num` as input and returns the sum of all its digits. The function should not use any built-in functions for converting numbers to strings or vice versa. After calculating the sum of digits, find the remainder when this sum is divided by 9.
"""

def sumDigits(num):
    if num == 0:
        return 0
    else:
        digit_sum = num % 10 + sumDigits(num // 10)
        return digit_sum % 9 if digit_sum >= 9 else digit_sum