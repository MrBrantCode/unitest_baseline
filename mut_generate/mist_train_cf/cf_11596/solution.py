"""
QUESTION:
Write a function called "power" that takes two numbers, base `a` and exponent `b`, as arguments. Implement the exponentiation algorithm manually without using built-in exponentiation functions or operators. Return the result of `a` raised to the power of `b`.
"""

def entance(a, b):
    result = 1
    if b >= 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(-b):
            result /= a
    return result