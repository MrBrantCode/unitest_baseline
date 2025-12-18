"""
QUESTION:
Write a function to find the sum of all numbers in a list that are divisible by 5 and less than 100. Use the built-in filter() function. The function should take a list of integers as input and return the sum of the filtered numbers.
"""

def entance(numbers):
    """Returns the sum of numbers in the list that are divisible by 5 and less than 100."""
    return sum(filter(lambda x: x % 5 == 0 and x < 100, numbers))