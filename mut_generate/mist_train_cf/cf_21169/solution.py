"""
QUESTION:
Write a function named `sum_elements` that takes a list of integers as input and returns the sum of all elements in the list that are greater than zero and less than or equal to 100. The list can contain up to 1 million elements.
"""

def sum_elements(lst):
    sum = 0
    for element in lst:
        if element > 0 and element <= 100:
            sum += element
    return sum