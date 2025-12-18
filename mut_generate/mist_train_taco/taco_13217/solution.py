"""
QUESTION:
# Task
Given two integers `a` and `b`, return the sum of the numerator and the denominator of the reduced fraction `a/b`.

# Example

For `a = 2, b = 4`, the result should be `3`

Since `2/4 = 1/2 => 1 + 2 = 3`.

For `a = 10, b = 100`, the result should be `11`

Since `10/100 = 1/10 => 1 + 10 = 11`.

For `a = 5, b = 5`, the result should be `2`

Since `5/5 = 1/1 => 1 + 1 = 2`.

# Input/Output


- `[input]` integer `a`

The numerator, `1 ≤ a ≤ 2000`.


- `[input]` integer `b`

The denominator, `1 ≤ b ≤ 2000`.


- `[output]` an integer

The sum of the numerator and the denominator of the reduces fraction.
"""

from math import gcd

def sum_of_reduced_fraction(a: int, b: int) -> int:
    """
    Calculate the sum of the numerator and the denominator of the reduced fraction a/b.

    Parameters:
    a (int): The numerator of the fraction.
    b (int): The denominator of the fraction.

    Returns:
    int: The sum of the numerator and the denominator of the reduced fraction.
    """
    gcd_value = gcd(a, b)
    reduced_numerator = a // gcd_value
    reduced_denominator = b // gcd_value
    return reduced_numerator + reduced_denominator