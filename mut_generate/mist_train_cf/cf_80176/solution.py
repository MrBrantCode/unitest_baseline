"""
QUESTION:
Write a function called `calculate_median` that takes a list of numbers as input and returns the median. If the list contains an even number of elements, the function should calculate the median as the arithmetic mean of the two middle numbers.
"""

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2