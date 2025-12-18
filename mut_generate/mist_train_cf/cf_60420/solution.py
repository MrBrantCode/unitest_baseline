"""
QUESTION:
Create a function `refine_sequence` that takes a list of integers as input and returns a new list containing only the elements that are divisible by 2 (even numbers).
"""

def refine_sequence(numbers):
    return [n for n in numbers if n % 2 == 0]