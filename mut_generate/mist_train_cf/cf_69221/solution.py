"""
QUESTION:
Create a function `multiply_elements` that takes an array of numbers as input. The function should initialize a variable to 1, then iterate over the array, multiplying the current product by each number in the array. The function should return the final product.
"""

def multiply_elements(input_array):
    product = 1
    for i in input_array:
        product *= i
    return product