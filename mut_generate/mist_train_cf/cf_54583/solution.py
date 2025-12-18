"""
QUESTION:
Write a function named `is_divisible_by_13` that takes a string representing a base 32 integer as input and returns a boolean value indicating whether the sum of the squares of the digits of the decimal equivalent of the input number is divisible by 13. The function should not take any additional arguments.
"""

def is_divisible_by_13(base32_num):
    decimal_num = int(base32_num, 32)
    sum_square_digits = sum(int(digit)**2 for digit in str(decimal_num))
    return sum_square_digits % 13 == 0