"""
QUESTION:
Write a function called `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion. The function must not use the multiplication operator (*) or the division operator (/). The function should return 1 if `n` is 0 or 1, and should return an error message if `n` is a negative number.
"""

def factorial(n):
    def add(a, b):
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

    def subtract(a, b):
        while b != 0:
            borrow = (~a) & b
            a = a ^ b
            b = borrow << 1
        return a

    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Factorial is not defined for negative numbers"
    else:
        return add(n, factorial(subtract(n, 1)))