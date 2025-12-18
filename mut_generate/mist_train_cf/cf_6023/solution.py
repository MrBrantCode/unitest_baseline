"""
QUESTION:
Write a recursive function `factorial(n)` to calculate the factorial of a given number `n` without using any arithmetic operators (+, -, *, /) or built-in mathematical functions. The function should only use bitwise operators and recursion.
"""

def entance(n):
    def multiply(a, b):
        if b == 0:
            return 0
        return add(a, multiply(a, subtract(b, 1)))

    def subtract(a, b):
        if b == 0:
            return a
        return subtract(a ^ b, (~a & b) << 1)

    def add(a, b):
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

    if n == 0:
        return 1
    return multiply(n, entance(subtract(n, 1)))