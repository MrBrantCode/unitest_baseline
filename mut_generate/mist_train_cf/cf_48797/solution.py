"""
QUESTION:
Write a Python 3 function named `process_list` that takes a list of integers as input, computes the product of all the integers in the list, and returns the result. The input list is obtained by taking a space-separated string of integers from user input and converting it into a list of integers. Ensure that the logic is split into separate functions, each handling a specific part: getting user input, converting input to list of integers, and processing the list. Implement suitable test cases to ensure correctness. The function `process_list` should use the `reduce` function from the `functools` module to compute the product.
"""

from functools import reduce

def process_list(int_list):
    return reduce(lambda x, y: x*y, int_list)