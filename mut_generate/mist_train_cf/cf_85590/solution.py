"""
QUESTION:
Design a function named 'sqrt' to calculate the square root of a number 'n' without using the square root function. The function should take one argument 'n' and return its approximate square root. The function should be able to calculate the square root up to a certain precision.
"""

def sqrt(n):
    # Making an initial guess
    x = n / 2

    while True:
        # Calculating a better guess
        better_guess = (x + n / x) / 2

        # If the better guess is good enough (the difference is very small), return it
        if abs(x - better_guess) < 0.000001:
            return better_guess

        # Otherwise, repeat with the better guess
        x = better_guess