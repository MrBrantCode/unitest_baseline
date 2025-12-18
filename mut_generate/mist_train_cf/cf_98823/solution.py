"""
QUESTION:
Create a function called `add_fractions` that takes two fractions as input in the form of tuples (numerator, denominator) and returns the sum of the fractions as a simplified fraction. The function should be able to handle improper fractions and mixed numbers. 

The input fractions are in the form of tuples where the first element of the tuple is the numerator and the second element is the denominator. The output should also be a tuple representing the simplified fraction.
"""

import math

def add_fractions(fraction1, fraction2):
    num1, den1 = fraction1
    num2, den2 = fraction2
    common_den = den1 * den2 // math.gcd(den1, den2)
    num_sum = num1 * common_den // den1 + num2 * common_den // den2
    common_factor = math.gcd(num_sum, common_den)
    return (num_sum // common_factor, common_den // common_factor)