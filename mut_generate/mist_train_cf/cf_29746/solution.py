"""
QUESTION:
Write a function `calculate_average_fractions` that takes a list of tuples as input, where each tuple contains an integer ID and a pair of integers representing a fraction. The function should calculate the average of the fractions and return the result rounded to the nearest integer.

The input list of tuples has the following structure: `List[Tuple[int, Tuple[int, int]]]`. The function should return an integer representing the average of the fractions.
"""

from typing import List, Tuple

def calculate_average_fractions(fractions: List[Tuple[int, Tuple[int, int]]]) -> int:
    total_numerator = 0
    total_denominator = 0

    for _, fraction in fractions:
        numerator, denominator = fraction
        total_numerator += numerator
        total_denominator += denominator

    average_fraction = total_numerator / total_denominator
    return round(average_fraction)