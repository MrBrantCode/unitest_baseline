"""
QUESTION:
Write a function `sum_of_fractions` that takes an integer `numerator` as input and returns a string representing the sum of fractions in its simplest form. The sum of fractions should be calculated by iterating over denominators from `numerator+1` to 99, where the numerator is fixed. The string should be in the format "X/Y", where X is the numerator and Y is the denominator of the simplified sum.
"""

from fractions import Fraction

def sum_of_fractions(numerator):
    total_sum = 0
    for denominator in range(numerator+1, 100):
        total_sum += Fraction(numerator, denominator)
    simplified_sum = total_sum.limit_denominator()
    return str(simplified_sum.numerator) + "/" + str(simplified_sum.denominator)