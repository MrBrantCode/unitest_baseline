"""
QUESTION:
Write a function `fibonacci_in_binary(n)` that calculates the n-th Fibonacci number and returns its binary representation as a string. The function should handle cases where n is less than 2 correctly and efficiently. It should use constant space, regardless of the value of n.
"""

def fibonacci_in_binary(n):
    if n < 2:
        return bin(n)[2:]
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return bin(b)[2:]