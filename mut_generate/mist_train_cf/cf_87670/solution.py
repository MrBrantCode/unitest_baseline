"""
QUESTION:
Write a function called `square_numbers` that takes a list of numbers as input and returns a new list with the squares of each number. The function should not modify the original list.
"""

def square_numbers(numbers):
    return [num ** 2 for num in numbers]