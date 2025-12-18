"""
QUESTION:
Create a function called `is_prime` that takes an integer `x` as input and returns `True` if `x` is a prime number and `False` otherwise. The function should not use the modulo operator (`%`) to check divisibility, instead using bitwise operations or other mathematical techniques.
"""

def entrance(x):
    # Special case for 1 and 2
    if x == 1 or x == 2:
        return True
    
    # Check if x is divisible by any number from 2 to sqrt(x)
    for i in range(2, int(x**0.5) + 1):
        if x // i * i == x:
            return False
    
    return True