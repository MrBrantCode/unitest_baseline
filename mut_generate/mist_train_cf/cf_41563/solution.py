"""
QUESTION:
Implement the `area_under_parametric_curve` function that calculates the approximate area under a parametric curve defined by two functions x(t) and y(t) using the trapezoidal rule. The function should take as input the functions x(t) and y(t), the range U of the parameter t, and the increment d. The range U is a positive real number, and the increment d is a positive real number.
"""

def area_under_parametric_curve(x, y, U, d):
    n = int(U / d)  
    area = 0.0
    for i in range(n):
        t1 = i * d
        t2 = (i + 1) * d
        x1, y1 = x(t1), y(t1)  
        x2, y2 = x(t2), y(t2)  
        area += 0.5 * (x1 + x2) * (y2 - y1)  
    return area