"""
QUESTION:
Implement a function `calculate_standard_deviation` that takes a list of numbers as input and returns the standard deviation of the input set. The solution should have a time complexity of O(n) and should not use any built-in functions or libraries for calculating standard deviation. The input list is guaranteed to have a length of at least 100 and all numbers are between -1000 and 1000.
"""

def calculate_standard_deviation(numbers):
    n = len(numbers)
    mean = sum(numbers) / n

    squared_differences = [(x - mean) ** 2 for x in numbers]
    sum_squared_differences = sum(squared_differences)

    variance = sum_squared_differences / n
    standard_deviation = variance ** 0.5

    return standard_deviation