"""
QUESTION:
Write a function `decimalToBinary(n)` that takes a decimal number `n` as input and returns its binary representation as a string without using any built-in functions or libraries for number conversion. The solution must have a time complexity of O(log n), where n is the given decimal number.
"""

def decimalToBinary(n):
    if n == 0:
        return ''
    elif n % 2 == 0:
        return decimalToBinary(n // 2) + '0'
    else:
        return decimalToBinary((n - 1) // 2) + '1'