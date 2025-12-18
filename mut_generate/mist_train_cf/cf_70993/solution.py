"""
QUESTION:
Create a Python function named `filter_even_numbers` that takes a list of inputs as an argument. This function should return a new list containing only the even integers from the input list. The input list can contain a mix of integers (positive, negative, and zero), non-integer numbers, and non-numeric characters. The function should ignore non-integer inputs.
"""

def filter_even_numbers(lst):
    # Filter only integers and even numbers using list comprehension
    return [i for i in lst if isinstance(i, int) and i % 2 == 0]