"""
QUESTION:
Create a function `trapezoidal_rule_area` that takes a function `func`, a lower limit of integration `xmin`, an upper limit of integration `xmax`, and a number of subintervals `n` to approximate the area under the curve using the trapezoidal rule. The function should return the approximate area under the curve.
"""

import numpy as np

def trapezoidal_rule_area(func, xmin, xmax, n):
    x = np.linspace(xmin, xmax, n+1)  
    y = func(x)  
    h = (xmax - xmin) / n  

    area = h * (0.5 * y[0] + 0.5 * y[-1] + np.sum(y[1:-1]))

    return area