"""
QUESTION:
Write a function called `find_y_limits` that takes three quadratic equations as input and returns the minimum and maximum y-values for a given range of x-values. The equations should be in the form of y = ax^2 + bx + c, where a, b, and c are constants. The range of x-values should be from -10 to 10.
"""

import numpy as np

def find_y_limits(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    def equation1(x):
        return a1*x**2 + b1*x + c1

    def equation2(x):
        return a2*x**2 + b2*x + c2

    def equation3(x):
        return a3*x**2 + b3*x + c3

    x_values = np.linspace(-10, 10, 1000)
    
    ymin1, ymax1 = min(equation1(x_values)), max(equation1(x_values))
    ymin2, ymax2 = min(equation2(x_values)), max(equation2(x_values))
    ymin3, ymax3 = min(equation3(x_values)), max(equation3(x_values))
    
    return ymin1, ymax1, ymin2, ymax2, ymin3, ymax3