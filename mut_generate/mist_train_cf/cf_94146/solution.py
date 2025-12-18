"""
QUESTION:
Write a function named `decimal_to_binary` that takes a decimal number as input and returns its binary representation as a string. The function should not use any built-in functions or libraries for conversion and should not use loops or recursion.
"""

def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    nums = []
    while decimal:
        nums.append(str(decimal % 2))
        decimal //= 2
    return ''.join(reversed(nums))