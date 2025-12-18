"""
QUESTION:
Write a function `sum_unique_even_numbers` that takes a list of integers as input and returns the sum of all unique even numbers in the list. The function should ignore duplicates and only consider each even number once.
"""

def sum_unique_even_numbers(numbers):
    return sum(set(number for number in numbers if number % 2 == 0))