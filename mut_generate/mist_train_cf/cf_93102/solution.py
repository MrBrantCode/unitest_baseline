"""
QUESTION:
Create a function `sin_degrees(x, iterations)` that takes in an angle in degrees and the number of iterations, and returns the approximate value of sin(x) using the Taylor series expansion. The function should not use the math module or any built-in trigonometric functions. The angle should be converted from degrees to radians before calculating the Taylor series.
"""

def sin_degrees(x, iterations=10):
    x_rad = x * (3.141592653589793238462643383279502884 / 180)
    
    result = term = x_rad
    
    for i in range(1, iterations):
        term *= -1 * (x_rad ** 2) / ((2 * i) * (2 * i + 1))
        
        result += term
    
    return result