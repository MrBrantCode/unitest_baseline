"""
QUESTION:
Write a function `find_max_number_and_index` that takes an array of integers as input. The function should return a tuple containing the maximum number in the array and its corresponding index. If multiple numbers have the same maximum value, the function should return the index of the first occurrence.
"""

def find_max_number_and_index(arr):
    """
    Returns a tuple containing the maximum number in the array and its corresponding index.
    
    If multiple numbers have the same maximum value, returns the index of the first occurrence.
    
    Args:
    arr (list): A list of integers.
    
    Returns:
    tuple: A tuple containing the maximum number and its index.
    """
    max_num = arr[0]
    max_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_index = i
            
    return max_num, max_index