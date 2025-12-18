"""
QUESTION:
Write a function `derivative(a, b)` that calculates the mathematical derivative of a quadratic function f(x) = ax^2 + bx + c, where 'a' and 'b' are the coefficients of x^2 and x respectively, and 'c' is the constant term. The function should return the derivative in the format "Derivative of f(x): {}x + {}".
"""

def derivative(a, b):
  # The derivative of x^2 is 2x, and the derivative of 5x is just 5.
  return "Derivative of f(x): {}x + {}".format(2*a, b)