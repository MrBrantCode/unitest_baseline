"""
QUESTION:
Write a function called `calculate_max_examples` that takes in a list of integers representing the potential values of variables and an integer representing the potential values of a class, and returns the maximum potential number of distinct examples that could be available. The function should assume that the number of variables and their potential values, as well as the number of class values, are fixed and provided as input.
"""

def calculate_max_examples(variables, class_values):
    number_of_examples = class_values
    for v in variables:
        number_of_examples *= v
    return number_of_examples