"""
QUESTION:
Write a function `calculate_product` that takes a nested list of positive integers as input and returns the product of all elements in the list. The input list may contain multiple sublists, and each sublist may contain one or more positive integers.
"""

def calculate_product(nested_list):
    product = 1
    for sublist in nested_list:
        for num in sublist:
            product *= num
    return product