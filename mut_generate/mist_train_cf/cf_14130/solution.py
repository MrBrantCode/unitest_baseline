"""
QUESTION:
Create a function called `sin_degrees(x, iterations=10)` that returns the approximate value of sin(x) in degrees without using the math module or any built-in trigonometric functions. The function should take two parameters: `x`, the angle in degrees, and `iterations`, the number of iterations to use in the Taylor series expansion (defaulting to 10).
"""

def sin_degrees(x, iterations=10):
    # Convert degrees to radians
    x_rad = x * (3.141592653589793238462643383279502884 / 180)
    
    # Initialize the result and the sign of the next term
    result = term = x_rad
    
    for i in range(1, iterations):
        # Calculate the next term in the series
        term *= -1 * (x_rad ** 2) / ((2 * i) * (2 * i + 1))
        
        # Add the next term to the result
        result += term
    
    return result