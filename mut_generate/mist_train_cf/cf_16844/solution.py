"""
QUESTION:
Write a function `calculate_standard_deviation(numbers)` that calculates the standard deviation of the input set of numbers with a time complexity of O(n) without using any built-in functions or libraries for standard deviation calculation. The function should handle negative numbers and return the calculated standard deviation.
"""

def entrance(numbers):
    n = len(numbers)
    mean = sum(numbers) / n

    squared_differences = [(x - mean) ** 2 for x in numbers]
    sum_squared_differences = sum(squared_differences)

    variance = sum_squared_differences / n
    standard_deviation = variance ** 0.5

    return standard_deviation