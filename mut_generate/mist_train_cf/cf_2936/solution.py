"""
QUESTION:
Write a function `evaluatePolynomial` that takes an integer `x` as input and evaluates the polynomial f(x) = 4x^3 + 7x^2 + 5x + 1 without using any loops or built-in mathematical functions. The function should use a recursive approach and handle the base cases accordingly.
"""

def evaluatePolynomial(x):
    def recursive_polynomial(n):
        if n == 0:
            return 1  # Base case: f(0) = 1
        else:
            return 4 * (x ** n) + recursive_polynomial(n - 1)  

    return recursive_polynomial(3)