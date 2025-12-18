"""
QUESTION:
Using Fermat's Little Theorem, write a function `power_mod(base, power, modulo)` that calculates the remainder when `base` raised to `power` is divided by a prime number `modulo`, where `base` is not divisible by `modulo`. The function should take three parameters: `base`, `power`, and `modulo`, and return the remainder of the division. Assume that the inputs will be integers, and `modulo` will be a prime number.
"""

def power_mod(base, power, modulo):
    """
    Calculate the remainder when 'base' raised to 'power' is divided by a prime number 'modulo'.
    
    Args:
    base (int): The base number.
    power (int): The power to which the base is raised.
    modulo (int): A prime number.

    Returns:
    int: The remainder of 'base' raised to 'power' divided by 'modulo'.
    """
    # Calculate the quotient and remainder
    quotient = power // (modulo - 1)
    remainder = power % (modulo - 1)
    
    # Calculate the result using Fermat's Little Theorem
    result = (pow(base, modulo - 1, modulo) ** quotient) % modulo * pow(base, remainder, modulo) % modulo
    
    return result