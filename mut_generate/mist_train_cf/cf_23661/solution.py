"""
QUESTION:
Create a function `filter_positive_numbers` that takes an array of integers as input and returns a new array containing only the positive numbers (including zero). The input array may contain both positive and negative integers, and may be empty.
"""

def filter_positive_numbers(arr):
    return [num for num in arr if num >= 0]