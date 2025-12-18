"""
QUESTION:
Implement a function named `square_root` that uses the Newton-Raphson method to find the square root of a given non-negative real number. The function should not use built-in square root functions and should iterate until the error is less than or equal to 0.00001. The function should return the approximate square root of the input number.
"""

def square_root(num: float) -> float:
    if num < 0:
        print("Square root of negative number is not defined in real numbers.")
        return None

    guess = num / 2.0  # Initial guess
    while True:
        better_guess = (guess + num / guess) / 2.0
        if abs(better_guess - guess) <= 0.00001:  
            return better_guess  # If the guess is accurate enough
        guess = better_guess  # Our new guess is the better one