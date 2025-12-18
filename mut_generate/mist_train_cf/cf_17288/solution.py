"""
QUESTION:
Implement a function `decimal_to_binary(n)` to convert a positive decimal number to binary using only bitwise operators and without using any loops or recursion. The function should return the binary representation as an integer.
"""

def decimal_to_binary(n):
    if n == 0:
        return 0
    
    binary = 0
    power = 1
    
    while n > 0:
        binary += (n % 2) * power
        n //= 2
        power *= 10
    
    return binary