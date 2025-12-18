"""
QUESTION:
Write a function `compute_product` that calculates the cumulative multiplication of all numbers in a given list. The function should initialize a variable to 1, then iterate over each number in the list, updating the variable by multiplying it with each number, and finally return the variable. The input list contains numbers from the Fibonacci series.
"""

def compute_product(list_nums):
    """
    This function calculates the cumulative multiplication of all numbers in a given list.
    
    Args:
    list_nums (list): A list of numbers.
    
    Returns:
    int: The cumulative product of all numbers in the list.
    """
    product = 1
    for num in list_nums:
        product *= num
    return product