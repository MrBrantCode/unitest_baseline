"""
QUESTION:
Implement the function `zdt3_eval` to evaluate the ZDT3 problem. The ZDT3 problem involves optimizing two conflicting objectives defined by the functions f1(x) and f2(x) with decision variables x = (x1, x2, ..., xn) in the range [0, 1]. The function f1(x) is defined as x1, and f2(x) is defined as g(x) * h(f1(x), g(x)), where g(x) and h(f1(x), g(x)) are defined as follows:

- g(x) = 1 + 9 * (Σ(xi) / (n-1))^0.25
- h(f1(x), g(x)) = 1 - sqrt(f1(x) / g(x)) - (f1(x) / g(x)) * sin(10 * π * f1(x))

The function `zdt3_eval` should take an individual (a list of decision variables) as input and return a tuple of two values representing the objective function values f1(x) and f2(x). 

Restrictions: The input individual is a list of real-valued numbers in the range [0, 1], and the output should be a tuple of two real-valued numbers.
"""

import numpy as np

def zdt3_eval(individual):
    """
    Evaluate the ZDT3 problem.

    Parameters:
    individual (list): A list of decision variables in the range [0, 1].

    Returns:
    tuple: A tuple of two real-valued numbers representing the objective function values f1(x) and f2(x).
    """
    f1 = individual[0]
    g = 1 + 9 * (np.sum(individual[1:]) / (len(individual) - 1))**0.25
    h = 1 - np.sqrt(f1 / g) - (f1 / g) * np.sin(10 * np.pi * f1)
    f2 = g * h
    return f1, f2