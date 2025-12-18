"""
QUESTION:
Create a function called `power_of_number` to calculate the exponentiation of two numbers. The function should take two parameters, `base` and `exponent`, and return the result of `base` raised to the power of `exponent`. The function should not use any built-in power functions, instead, it should use a loop to calculate the result.
"""

def power_of_number(base, exponent):
    """
    This function calculates the exponentiation of two numbers.
    
    Parameters:
    base (int): The base number
    exponent (int): The exponent to which the base is raised
    
    Returns:
    int: The result of base raised to the power of exponent
    """
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result
    else:
        return result