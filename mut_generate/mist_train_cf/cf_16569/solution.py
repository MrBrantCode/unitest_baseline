"""
QUESTION:
Write a function `calculate_median` that calculates the median of a given list of numbers. The function should be able to handle lists of any length, including both odd and even lengths, as well as lists containing duplicate numbers and floating-point numbers.
"""

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 1:
        return sorted_numbers[length // 2]
    else:
        mid1 = sorted_numbers[length // 2 - 1]
        mid2 = sorted_numbers[length // 2]
        return (mid1 + mid2) / 2