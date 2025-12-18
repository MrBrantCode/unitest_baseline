"""
QUESTION:
Write a function to calculate the median of a given set of numbers. The function should take a list of integers as input and return the median value. The input list can have an even or odd number of elements. If the number of elements is even, the median should be the average of the two middle elements. If the number of elements is odd, the median should be the middle element.
"""

def calculate_median(numbers):
    n = len(numbers)
    sorted_numbers = sorted(numbers)
    if n % 2 == 0:
        m = n // 2
        median = (sorted_numbers[m-1] + sorted_numbers[m]) / 2.0
    else:
        m = (n + 1) // 2
        median = sorted_numbers[m-1]
    return median