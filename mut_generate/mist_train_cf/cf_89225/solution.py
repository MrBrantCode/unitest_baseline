"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a given number `n` without using any arithmetic operators (+, -, *, /) or built-in mathematical functions. The function should return the factorial of `n` as an integer.
"""

def entance(n):
    def multiply(a, b):
        if b == 0:
            return 0
        return a + multiply(a, subtract(b, 1))

    def subtract(a, b):
        if b == 0:
            return a
        return subtract(a ^ b, (~a & b) << 1)

    if n == 0:
        return 1
    return multiply(n, entance(subtract(n, 1)))