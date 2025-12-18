"""
QUESTION:
Write a function named `decimal_to_binary` that takes a decimal value `n` as input and returns its binary equivalent as a string. The function should have a time complexity of O(log n), where n is the decimal value.
"""

def decimal_to_binary(n):
    if n == 0:
        return '0'

    binary = ''
    while n > 0:
        remainder = n % 2
        binary += str(remainder)
        n = n // 2

    return binary[::-1]