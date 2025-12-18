"""
QUESTION:
Write a function called `find_highest_even` that takes a list of integers as input and returns the highest even integer in the list. If the list does not contain any even integers, the function should return None.
"""

def find_highest_even(lst):
    even_numbers = [number for number in lst if number % 2 == 0]
    return max(even_numbers) if even_numbers else None