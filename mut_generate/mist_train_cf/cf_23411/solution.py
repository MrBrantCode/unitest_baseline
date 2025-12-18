"""
QUESTION:
Write a function `product_of_elements` that calculates the product of all elements in the input list. The function should accept a list of numbers as input and return the product of all numbers in the list.
"""

def product_of_elements(data):
    result = 1
    for num in data:
        result *= num
    return result