"""
QUESTION:
Write a function `check_even_product` that takes a list of integers as input and returns `True` if the product of any two integers in the list is even, and `False` otherwise. Assume that the input list contains at least one integer. The function should run in linear time.
"""

def check_even_product(num_list):
    # Iterate over every number in the list
    for num in num_list:
        # Check if the current number is even
        if num % 2 == 0:
            return True
    # If no even number has been found, return False
    return False