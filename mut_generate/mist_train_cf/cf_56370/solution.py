"""
QUESTION:
You are given a string that represents a mathematical expression involving the addition and subtraction of fractions. The function `add_subtract_fracs(math_expression)` should compute the result of the expression and return it in string format as a simplified fraction. If the result is a whole number, it should be represented with a denominator of 1. The input string only includes the characters '0' through '9', '/', '+', and '-', and each fraction (input and output) follows the format ±numerator/denominator. The quantity of fractions provided is within the range [1,10], and the numerator and denominator of each fraction and the final result are within the range of a 32-bit integer.
"""

import re
import fractions

def add_subtract_fracs(math_expression):
    fractions_list = re.findall('[+-]?[0-9]+/[0-9]+', math_expression)
    result = fractions.Fraction(0)
    for frac in fractions_list:
        result += fractions.Fraction(frac)

    if result.denominator == 1:
        result = fractions.Fraction(result.numerator, 1)
    
    return str(result)