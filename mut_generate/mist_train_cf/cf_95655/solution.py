"""
QUESTION:
Implement a function named `square_root` that calculates the square root of a given number using the Newton-Raphson method. The function should not use the built-in square root function or any math libraries. The result should be accurate up to 5 decimal places.
"""

def square_root(num):
    guess = num / 2  # initial guess is half of the number
    
    while True:
        new_guess = (guess + num / guess) / 2  # Newton-Raphson method
        
        # check if the new guess is accurate up to 5 decimal places
        if abs(new_guess - guess) < 0.00001:
            return round(new_guess, 5)
        
        guess = new_guess