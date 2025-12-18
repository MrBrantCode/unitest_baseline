"""
QUESTION:
Design a function `find_smallest_product` that takes an array of integers as input and returns the smallest possible product of a subarray where no two elements in the subarray are consecutive numbers. The function should also use two helper functions: `calculate_product` to calculate the product of a subarray between given start and end indexes, and `is_consecutive` to check if any consecutive numbers are present between the given indexes. The function should return the smallest product found.
"""

def calculate_product(array, start, end):
    """ Determine and return the product of elements in an array between the given start and end index."""
    product = 1
    for i in range(start, end + 1):
        product *= array[i]
    return product

def is_consecutive(array, start, end):
    """ Check if there are any successive elements present between start and end index."""
    for i in range(start, end):
        if array[i] + 1 == array[i + 1]:
            return True
    return False

def find_smallest_product(array):
    """ Determine the smallest potential product of a subarray where no two elements are successive 
    using the `is_consecutive` helper function. 
    """
    smallest_product = float('inf')
    for i in range(len(array)):
        for j in range(i, len(array)):
            subarray = array[i:j + 1]
            product = calculate_product(array, i, j)
            if not is_consecutive(subarray, 0, j - i) and product < smallest_product:
                smallest_product = product
    return smallest_product