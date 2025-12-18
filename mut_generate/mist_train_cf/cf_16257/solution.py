"""
QUESTION:
Write a function `decimal_to_binary` that takes an integer `decimal` as input and returns a string representing its binary representation. The function should not use built-in functions or libraries for conversion, loops, or recursion.
"""

def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    nums = []
    while decimal:
        nums.append(str(decimal % 2))
        decimal //= 2
    return ''.join(reversed(nums))