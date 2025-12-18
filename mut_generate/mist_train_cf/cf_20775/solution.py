"""
QUESTION:
Write a function named `get_odd_numbers` that takes a list of integers as input. The function should return a list containing only the odd numbers from the input list, sorted in descending order with no duplicates. If the input list contains no odd numbers, return an empty list.
"""

def get_odd_numbers(lst):
    # Filter out the odd numbers
    odd_numbers = [num for num in lst if num % 2 != 0]

    # If the resulting list is empty or contains only even numbers, return an empty list
    if len(odd_numbers) == 0:
        return []

    # Sort the odd numbers in descending order and remove duplicates
    return sorted(set(odd_numbers), reverse=True)