"""
QUESTION:
Implement a class `Linearithmic` that inherits from `calculus.Function` and represents a linearithmic function of the form f(x) = (mx + h)log_b(kx + a). The class should have an `__init__` method to initialize the parameters m, h, b, a, and k with default values m=1, h=0, b=10, a=0, and k=1. The class should also have an `evaluate` method that calculates and returns the value of the linearithmic function for a given input x.
"""

import math

def linearithmic(m=1, h=0, b=10, a=0, k=1):
    """
    Calculate the value of the linearithmic function f(x) = (mx + h)log_b(kx + a) for a given input x.
    :param m: coefficient of x
    :param h: constant term
    :param b: base of the logarithm
    :param a: constant term in the argument of the logarithm
    :param k: coefficient of x in the argument of the logarithm
    :param x: input value
    :return: value of the linearithmic function for the given input x
    """
    def calculate(x):
        return (m * x + h) * math.log(k * x + a, b)
    return calculate