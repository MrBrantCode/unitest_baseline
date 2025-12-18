"""
QUESTION:
Given a function transformation from f(x) = sin x to g(x) = 3 sin 2x, describe how this transformation affects the domain and range of the initial function f(x), and explain the mathematical interpretation of this change.
"""

import numpy as np

def transformed_function(x):
    return 3 * np.sin(2 * x)