"""
QUESTION:
Implement a function called `square_root` that takes a number as input and returns its square root accurate up to 5 decimal places using the Newton-Raphson method, without using the built-in square root function or any math libraries. The function should iteratively refine its guess until the difference between the new and old guesses is less than 0.00001.
"""

def square_root(num):
    guess = num / 2  # initial guess is half of the number
    
    while True:
        new_guess = (guess + num / guess) / 2  # Newton-Raphson method
        
        # check if the new guess is accurate up to 5 decimal places
        if abs(new_guess - guess) < 0.00001:
            return round(new_guess, 5)
        
        guess = new_guess