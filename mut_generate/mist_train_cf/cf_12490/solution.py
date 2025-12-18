"""
QUESTION:
Write a function named `sum_nested_product` that calculates the product of all elements in a given nested list. The function should take a 2D list of integers as input and return the product of all elements in the list.
"""

def sum_nested_product(nested_list):
    product = 1
    for sublist in nested_list:
        for element in sublist:
            product *= element
    return product