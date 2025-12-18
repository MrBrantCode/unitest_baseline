"""
QUESTION:
Write a function `calculate_median(numbers)` that takes a list of positive integers `numbers` as input, where the list length is odd and ranges from 1000 to 5000, and the numbers are in the range of 1 to 1000. The function should return the median value of the input list.
"""

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    middle_index = (len(sorted_numbers) + 1) // 2
    median = sorted_numbers[middle_index - 1]
    return median