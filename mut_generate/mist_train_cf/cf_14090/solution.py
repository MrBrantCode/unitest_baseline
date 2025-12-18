"""
QUESTION:
Write a function `sum_numbers` that takes a list as input and returns the sum of all numbers (integers and floats) in the list, including those in any nested lists. The function should ignore non-numeric elements (such as strings) and handle lists of arbitrary depth.
"""

def sum_numbers(lst):
    total = 0
    for element in lst:
        if type(element) == list:
            total += sum_numbers(element)
        elif type(element) in [int, float]:
            total += element
    return total