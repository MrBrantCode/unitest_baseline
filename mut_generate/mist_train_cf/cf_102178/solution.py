"""
QUESTION:
Create a generator expression named `generator_expression` that takes a list of numbers and returns the squared values of these numbers, excluding those that are divisible by both 2 and 3 or by 4 or 5, and only including those squared values that are divisible by 7.
"""

def generator_expression(list_of_nums):
    return (x**2 for x in list_of_nums if (x % 2 != 0 or x % 3 != 0) and (x % 4 != 0 and x % 5 != 0) and x**2 % 7 == 0)