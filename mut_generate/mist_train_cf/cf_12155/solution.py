"""
QUESTION:
Write a function `filter_numbers` that takes a list of integers as input and returns a new list containing all numbers from the original list that are not between 100 and 1000 (exclusive). The function should not modify the original list. The input list may contain negative numbers, zeros, and numbers larger than 1000.
"""

def filter_numbers(numbers):
    return [num for num in numbers if not 100 < num < 1000]