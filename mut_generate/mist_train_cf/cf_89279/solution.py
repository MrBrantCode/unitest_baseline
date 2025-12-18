"""
QUESTION:
Implement a function `modulo(a, b, c)` that calculates `(a^b) % c` efficiently. The function should take three integers `a`, `b`, and `c` as input and return the result of the modular exponentiation. The time complexity should be O(log n), where n is the exponent `b`. The space complexity should be O(1).
"""

def modulo(a, b, c):
    result = 1
    a = a % c

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c

        b = b >> 1
        a = (a ** 2) % c

    return result