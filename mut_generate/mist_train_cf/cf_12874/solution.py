"""
QUESTION:
Write a function named `sum_even_numbers` that calculates the sum of all even integers in a given list. The list may contain non-numeric elements, which should be ignored in the calculation. The function should return the sum as an integer.
"""

def sum_even_numbers(lst):
    total = 0
    for element in lst:
        if isinstance(element, int) and element % 2 == 0:
            total += element
    return total