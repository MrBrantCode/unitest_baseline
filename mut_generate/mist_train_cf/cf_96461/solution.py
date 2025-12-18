"""
QUESTION:
Implement a function named `sum_elements` that takes a list of integers as input and returns the sum of all elements in the list that are greater than 0 and less than or equal to 100. The function should be able to handle lists with up to 1 million elements.
"""

def sum_elements(lst):
    return sum(i for i in lst if 0 < i <= 100)