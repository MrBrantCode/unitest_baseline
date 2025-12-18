"""
QUESTION:
Write a function `find_max_number` that takes an array of integers as input and returns the maximum number in the array. The function should not use any built-in max/min functions.
"""

def find_max_number(array):
    """
    This function takes an array of integers as input and returns the maximum number in the array.
    
    Parameters:
    array (list): A list of integers.
    
    Returns:
    int: The maximum number in the array.
    """
    maxNum = array[0]
    for num in array: 
        if num > maxNum: 
            maxNum = num 
    return maxNum