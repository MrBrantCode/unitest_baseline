"""
QUESTION:
Write a function `sort_even_numbers` that takes a list of integers as input, removes all elements that are odd or greater than 10, and returns the remaining even numbers in descending order.
"""

def sort_even_numbers(lst):
    return sorted([num for num in lst if num % 2 == 0 and num <= 10], reverse=True)