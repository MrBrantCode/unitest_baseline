"""
QUESTION:
Write a function named `calculate_median` that takes a list of numbers as input and returns the median value. The function should handle lists with both odd and even numbers of elements.
"""

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        middle_right = n // 2
        middle_left = middle_right - 1
        median = (numbers[middle_left] + numbers[middle_right]) / 2
    else:
        median = numbers[n // 2]
    return median