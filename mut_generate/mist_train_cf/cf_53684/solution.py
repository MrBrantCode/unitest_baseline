"""
QUESTION:
Create a function named `sort_in_descending_order` that takes a list of integers as input and returns the list in descending order without any distinction between prime and composite numbers. The function should use the native list sort method and not require any external libraries.
"""

def sort_in_descending_order(numbers):
    numbers.sort(reverse=True)
    return numbers