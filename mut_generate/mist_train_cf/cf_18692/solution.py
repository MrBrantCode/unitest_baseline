"""
QUESTION:
Write a function `remove_duplicates` that takes a list of integers as input, removes duplicates and negative numbers, and returns the distinct non-negative integers in descending order.
"""

def remove_duplicates(numbers):
    distinct_numbers = list(set(numbers)) # Remove duplicates
    distinct_numbers = [num for num in distinct_numbers if num >= 0] # Remove negatives
    distinct_numbers.sort(reverse=True) # Sort in descending order
    return distinct_numbers