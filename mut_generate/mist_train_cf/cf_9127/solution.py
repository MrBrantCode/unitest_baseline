"""
QUESTION:
Write a function called `filter_even_numbers` that takes a list of integers as input, filters out the even numbers, and returns them in a new sorted list in ascending order. The function should not modify the original list.
"""

def filter_even_numbers(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    even_numbers.sort()
    return even_numbers