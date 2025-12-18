"""
QUESTION:
Create a function named `descending_squares` that takes a list of integers as input, squares each integer, and returns a new list containing the squared values in descending order.
"""

def descending_squares(numbers):
    return sorted([i ** 2 for i in numbers], reverse=True)