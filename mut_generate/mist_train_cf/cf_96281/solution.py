"""
QUESTION:
Write a function named `get_odd_numbers` that takes a list of integers as input and returns a new list containing the unique odd numbers from the original list, sorted in descending order. If the input list is empty or contains only even numbers, return an empty list.
"""

def get_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    if len(odd_numbers) == 0:
        return []
    odd_numbers = sorted(list(set(odd_numbers)), reverse=True)
    return odd_numbers