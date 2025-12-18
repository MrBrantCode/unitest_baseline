"""
QUESTION:
Write a function `find_roots(a, b, c, d)` that calculates the roots of the cubic equation ax^3 + bx^2 + cx + d = 0. If the roots are complex, specify this. Account for possible cases where there might be less than three roots.
"""

import numpy as np

def find_roots(a, b, c, d):
    coefficients = [a, b, c, d]
    roots = np.roots(coefficients)
    
    is_real = list(map(np.isreal, roots))

    if all(is_real):
        return "All roots are real. Roots are: " + str(roots)
    else:
        result = "Some roots are complex. Roots are: "
        for i, x in enumerate(roots):
            if is_real[i]:
                result += "Root {} is a real number: {}, ".format(i+1, x)
            else:
                result += "Root {} is a complex number: {}, ".format(i+1, x)
        return result