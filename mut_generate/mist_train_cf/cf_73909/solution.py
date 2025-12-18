"""
QUESTION:
Write a function named `median` that calculates the median of a list of numbers. The function should work correctly for any valid input of integers or floating-point numbers. The input list is not sorted, and the function should handle both even and odd lengths of lists. The function should return the median value as a float.
"""

def median(numbers):
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        return (numbers[length // 2] + numbers[length // 2 - 1]) / 2
    else:
        return numbers[length // 2]