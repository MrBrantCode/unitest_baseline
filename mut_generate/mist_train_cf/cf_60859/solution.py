"""
QUESTION:
Write a function `calculate_stats(n)` to calculate the sum, average, and standard deviation of the first n natural numbers. The function should take an integer n as input and return a tuple of three values: the sum of the first n natural numbers, their average, and their standard deviation. The standard deviation should be calculated using the population standard deviation formula.
"""

import math

def calculate_stats(n):
    natural_numbers = [i for i in range(1, n+1)]
    sum_numbers = sum(natural_numbers)
    average = sum_numbers/n
    squares = [(i - average) ** 2 for i in natural_numbers]
    std_dev = math.sqrt(sum(squares) / n)
    return sum_numbers, average, std_dev