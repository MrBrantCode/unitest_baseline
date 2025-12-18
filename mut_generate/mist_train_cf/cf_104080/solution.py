"""
QUESTION:
Write a function `compute_product(arr)` that takes an array of integers as input and returns the product of all even elements. If the array does not contain any even elements, the function should return 1.
"""

def compute_product(arr):
    """
    Compute the product of all even elements in an array.
    
    If the array does not contain any even elements, return 1.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The product of all even elements in the array.
    """
    product = 1
    for num in arr:
        if num % 2 == 0:
            product *= num
    return product