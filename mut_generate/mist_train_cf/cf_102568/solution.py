"""
QUESTION:
Write a function called `get_even_numbers` that takes a list of integers as input and returns a new list containing only the even numbers from the input list. The function should not modify the original list.
"""

def get_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))