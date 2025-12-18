"""
QUESTION:
Write a recursive function called `int_to_string(n)` that converts a given integer `n` into its string representation. The function should handle negative numbers and convert them into a string with a negative sign. The input `n` is an integer and can be any 32-bit signed integer.
"""

def int_to_string(n):
    if n < 0:
        return '-' + int_to_string(-n)
    if n < 10:
        return chr(ord('0') + n)
    return int_to_string(n // 10) + chr(ord('0') + n % 10)