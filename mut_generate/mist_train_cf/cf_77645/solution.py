"""
QUESTION:
Write a function `calculate_mean` that takes a list of integers as input and returns the numerical mean of the collection. The function should handle the calculation by summing all the numbers in the list and dividing by the total count of numbers.
"""

def calculate_mean(lst):
    return sum(lst) / len(lst)