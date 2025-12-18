"""
QUESTION:
Write a Python function `decimal_to_binary(n)` that takes a non-negative integer `n` and returns its binary representation as a string using recursive programming. The function should not have any side effects such as printing to the console.
"""

def decimal_to_binary(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return decimal_to_binary(n // 2) + str(n % 2)