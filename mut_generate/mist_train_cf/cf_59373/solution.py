"""
QUESTION:
Write a function `decimal_to_binary(n)` that converts a decimal number `n` to its binary representation as a string, without using built-in decimal to binary conversion methods. The output should not contain leading zeros unless `n` is zero.
"""

def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary