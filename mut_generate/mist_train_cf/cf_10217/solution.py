"""
QUESTION:
Calculate the standard deviation of a set of numbers without using built-in functions or libraries. The input set of numbers has a length of at least 100 and a maximum value of 1000, and the solution should have a time complexity of O(n). Implement a function `calculate_standard_deviation(numbers)` to compute the standard deviation.
"""

def calculate_standard_deviation(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
    variance = squared_diff_sum / n
    standard_deviation = variance ** 0.5
    return standard_deviation