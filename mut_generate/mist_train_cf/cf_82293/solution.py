"""
QUESTION:
Write a function `calculate_products(array)` that accepts a three-dimensional array as an argument and returns both the product of the elements in the array and the product of the sums at each depth level. The function should handle arrays with any number of elements at each level, including empty sub-arrays, arrays with one element, and arrays with negative numbers.
"""

from functools import reduce
import operator

def calculate_products(array):
    # Initialize total_product and depth_sums_product
    total_product = None
    depth_sums_product = None
    
    # Flatten the 3D array into 1D for calculating total_product
    flattened_array = [num for sublist1 in array for sublist2 in sublist1 for num in sublist2]
    
    # Calculate total_product (product of all elements)
    if flattened_array:  
        total_product = reduce(operator.mul, flattened_array, 1)
    
    # Calculate sums at each depth level
    depth_sums = [sum(map(sum, sublist)) for sublist in array]
    
    # Calculate depth_sums_product
    depth_sums_product = reduce(operator.mul, depth_sums, 1) if depth_sums else None
    
    return total_product, depth_sums_product