"""
QUESTION:
Create a function called `prime_factors` that takes an integer `number` as input and returns the distinct prime factors of the number. The function should return these factors as a set. 

Also, create a Boolean expression to check if a number is a multiple of both 5 and 7, is greater than 100, and has exactly three distinct prime factors.

Restrictions: The code should be written in Python and the Boolean expression should use the `prime_factors` function.
"""

def prime_factors(number):
    """
    Returns the distinct prime factors of a number as a set.
    
    Args:
    number (int): The number to find prime factors for.
    
    Returns:
    set: A set of distinct prime factors of the number.
    """
    factors = set()
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.add(i)
    if number > 1:
        factors.add(number)
    return factors