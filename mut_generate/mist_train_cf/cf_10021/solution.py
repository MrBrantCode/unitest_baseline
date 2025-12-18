"""
QUESTION:
Write a function called `calculate_median` that calculates the median of a given list of numbers. The function should take a list of numbers as input and return the median. The list may contain an odd or even number of elements, and it is assumed that the list only contains numeric elements.
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