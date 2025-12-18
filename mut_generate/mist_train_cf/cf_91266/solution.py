"""
QUESTION:
Write a function named `calculate_standard_deviation` that calculates the standard deviation of a given set of numbers with a time complexity of O(n) without using any built-in functions or libraries for calculating standard deviation. The input set will have at least 100 numbers and a maximum value of 1000.
"""

def calculate_standard_deviation(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
    variance = squared_diff_sum / n
    standard_deviation = variance ** 0.5
    return standard_deviation