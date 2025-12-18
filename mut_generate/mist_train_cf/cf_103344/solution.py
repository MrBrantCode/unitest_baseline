"""
QUESTION:
Implement a function `square_root(number)` that uses the Newton-Raphson method to find the square root of a given number. The function should accept a single argument `number` and return the approximate square root of the number. The precision of the result can be improved by increasing the maximum number of iterations, which should be capped at a reasonable limit to prevent infinite loops.
"""

def square_root(number):
    # Initial guess for the square root
    x = number / 2
    
    # Maximum number of iterations
    max_iterations = 1000
    
    # Iterate until desired precision is achieved or maximum iterations are reached
    for _ in range(max_iterations):
        # Update the guess using the Newton-Raphson method
        x = (x + number / x) / 2
        
    return x