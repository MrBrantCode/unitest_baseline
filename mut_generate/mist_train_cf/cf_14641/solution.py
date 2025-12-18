"""
QUESTION:
Find the derivative of a given polynomial equation with respect to x using the power rule and return the result in the simplified form ax^n + bx^(n-1) + cx^(n-2) + ... + k. The input equation will be a polynomial of the form ax^n + bx^(n-1) + cx^(n-2) + ... + k, where a, b, c, ..., k are coefficients.
"""

def find_derivative(equation):
    derivative = []
    for degree, coeff in equation.items():
        if degree != 0:
            derivative.append((coeff * degree, degree - 1))
    return derivative

# the function takes a dictionary where the key is the power and the value is the coefficient
# for example the equation y = 3x^2 + 4x - 2 is written as {2: 3, 1: 4, 0: -2}