"""
QUESTION:
Write a function named `unique_product` that takes a list of numbers as input, calculates the product of its unique elements, and returns the result. The function should exclude any repeated elements in the computation process.
"""

def unique_product(lst):
    # Convert list to a set to remove duplicates
    unique_lst = set(lst)
    # Initialize product as 1
    product = 1
    # Iterate through unique list and multiply numbers
    for num in unique_lst:
        product *= num
    return product