"""
QUESTION:
Create a function named `get_odd_numbers` that takes a list of integers as input and returns a new list containing only the unique odd numbers from the original list in ascending order.
"""

def get_odd_numbers(input_list):
    return sorted(set([num for num in input_list if num % 2 != 0]))