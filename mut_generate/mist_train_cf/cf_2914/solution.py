"""
QUESTION:
Write a function named `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion, without using the multiplication or division operators, and without using any loops. The function should handle negative inputs and return `None` in such cases.
"""

def factorial(n):
    def multiply(a, b):
        if b == 0:
            return 0
        if b < 0:
            return -multiply(a, -b)
        return a + multiply(a, b-1)

    def subtract(a, b):
        def add(a, b):
            if b == 0:
                return a
            if b < 0:
                return subtract(a, -b)
            return add(a+1, b-1)
        if b == 0:
            return a
        if b < 0:
            return add(a, -b)
        return subtract(a-1, b-1)

    if n < 0:
        return None
    if n == 0:
        return 1
    return multiply(n, factorial(subtract(n, 1)))