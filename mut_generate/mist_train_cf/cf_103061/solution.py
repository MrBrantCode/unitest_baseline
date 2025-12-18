"""
QUESTION:
Write a function named `filter_odd_numbers` that takes a list of integers as input, uses a lambda expression to filter out even numbers, and returns a new list containing only the odd numbers. The function should not take any other parameters.
"""

def filter_odd_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))