"""
QUESTION:
Write a function `decimalToBinary(n)` that takes a decimal number `n` as input and returns its binary representation as a string, with a time complexity of O(log n).
"""

def decimalToBinary(n):
    if n == 0:
        return ''
    elif n % 2 == 0:
        return decimalToBinary(n // 2) + '0'
    else:
        return decimalToBinary((n - 1) // 2) + '1'