"""
QUESTION:
Write a function named `second_largest` that takes a list of integers as input and returns the second largest distinct number. If there is no second largest distinct number, return -1. The input list can contain duplicates.
"""

def second_largest(numbers):
    distinct_numbers = sorted(set(numbers), reverse=True)
    if len(distinct_numbers) < 2:
        return -1
    return distinct_numbers[1]