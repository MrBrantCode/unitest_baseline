"""
QUESTION:
Write a function named `decimal_to_binary` that takes an integer `n` as input and returns its binary equivalent as a string. The function should have a time complexity of O(log n). If the input is 0, return '0'.
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