"""
QUESTION:
Write a function named 'array_sum' that takes a 2D array of numbers as input and returns the sum of all elements in the array. The array can contain any number of rows and columns, and the elements are numbers.
"""

def array_sum(arr):
    """
    This function calculates the sum of all elements in a 2D array.
    
    Parameters:
    arr (list): A 2D array of numbers.
    
    Returns:
    int: The sum of all elements in the array.
    """
    total_sum = 0
    for row in arr:
        for el in row: 
            total_sum += el 
    return total_sum