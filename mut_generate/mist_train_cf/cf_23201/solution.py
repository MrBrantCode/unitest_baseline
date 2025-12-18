"""
QUESTION:
Write a function `filter_even_numbers` that takes a list of integers as input and returns a new list containing only the even numbers from the input list. Use the `filter` function in combination with a lambda function to achieve this.
"""

def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))