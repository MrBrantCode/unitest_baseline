"""
QUESTION:
Write a function named decimalToBinary that takes an integer n as input and returns its binary representation. The function should not use any built-in functions for binary conversion and should work for any non-negative integer n.
"""

def decimalToBinary(n):
    if (n == 0):
        return 0
    else:
        return (n % 2 + 10 *
                decimalToBinary(int(n // 2)))