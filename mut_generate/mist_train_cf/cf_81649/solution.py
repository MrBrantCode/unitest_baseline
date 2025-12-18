"""
QUESTION:
Implement a function `cube_root_newton(num)` that uses Newton's method to calculate the cube root of a given number `num`. The function should take a single argument `num` and return its cube root. The precision of the result should be within `0.01`.
"""

def cube_root_newton(num):
    # Set an initial guess
    guess = num / 3
    epsilon = 0.01

    # Iterate using Newton's method
    while abs(guess**3 - num) >= epsilon:
        guess = guess - ((guess**3 - num) / (3 * guess**2))
        
    return guess