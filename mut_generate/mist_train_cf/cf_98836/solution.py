"""
QUESTION:
Create a function `calculate_result(a, b, c)` that takes three integers `a`, `b`, and `c` as input and returns the value of `a` raised to the power of `b`, multiplied by `c` raised to the power of the product of `a` and `b`, and finally divided by `2` raised to the power of the sum of `a`, `b`, and `c`. The function should also check that `a` and `b` are both even, while `c` is odd, and return an error message if this condition is not met.
"""

def calculate_result(a, b, c):
    """
    This function calculates the result of a raised to the power of b, 
    multiplied by c raised to the power of the product of a and b, 
    and finally divided by 2 raised to the power of the sum of a, b, and c.

    Args:
    a (int): The base number.
    b (int): The exponent.
    c (int): The base for the second term.

    Returns:
    float: The result of the calculation.
    str: An error message if a and b are not even or c is not odd.

    """
    # Checking that a and b are even while c is odd
    if a % 2 == 0 and b % 2 == 0 and c % 2 != 0:
        # Calculating value of a raised to the power of b
        ab = a ** b

        # Calculating value of c raised to the power of the product of a and b
        cab = c ** (a * b)

        # Calculating value of 2 raised to the power of the sum of a, b, and c
        twosum = 2 ** (a + b + c)

        # Calculating the final result
        result = (ab * cab) / twosum
        return result
    else:
        return "Invalid values of a, b, and c"