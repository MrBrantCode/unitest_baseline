"""
QUESTION:
Implement a function `decimal_to_binary(n)` that takes a positive decimal number `n` as input and returns its binary representation as a decimal number using only bitwise operators and without using any loops or recursion.
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