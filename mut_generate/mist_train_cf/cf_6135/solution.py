"""
QUESTION:
Implement a function named `modulo` that takes three integers `a`, `b`, and `c` as input and returns the result of `(a^b) % c` using modular exponentiation. The function should have a time complexity of O(log n), where n is the exponent `b`. The space complexity should be O(1).
"""

def modulo(a, b, c):
    result = 1
    a = a % c

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c

        b = b >> 1
        a = (a * a) % c

    return result