"""
QUESTION:
Given a non-increasing sequence of integers generated from a positive real value φ, find the only value of φ for which the generated sequence starts at c1 = 3 and the concatenation of the generated sequence equals the original value φ, rounded to 24 decimal places. The sequence is generated using the following recursive formula:

dn = ⌈dn-1⌉(dn-1 - ⌈dn-1⌉ + 1) and cn = ⌈dn⌉

where ⌈⋅⌉ is the ceiling function. Implement a function that finds the value of φ within a specified precision using a bisection search approach.
"""

import math

def entrance(c1, phi_min, phi_max, precision):
    """
    Find the value of φ within a specified precision using a bisection search approach.

    Args:
    c1 (float): The first term in the sequence.
    phi_min (float): The minimum value of φ.
    phi_max (float): The maximum value of φ.
    precision (float): The desired precision.

    Returns:
    float: The value of φ.
    """

    while phi_max - phi_min > precision:
        phi_guess = (phi_min + phi_max) / 2
        d = phi_guess
        sigma, concat_multiplier = c1, 0.1
        next_int, d = math.modf(d)

        while next_int > precision:
            d = math.ceil(d) * next_int
            next_int, d = math.modf(d)
            sigma += d * concat_multiplier
            concat_multiplier /= 10 ** math.ceil(math.log10(d + 1))

        if sigma > phi_guess:
            phi_max = phi_guess
        else:
            phi_min = phi_guess

    return (phi_min + phi_max) / 2