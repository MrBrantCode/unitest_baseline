"""
QUESTION:
Write a function named `second_largest_index` that finds the index of the second largest element in an array of integers. The array is guaranteed to have at least two unique elements.
"""

def second_largest_index(arr):
    """
    This function finds the index of the second largest element in an array of integers.
    
    Parameters:
    arr (list): A list of integers with at least two unique elements.
    
    Returns:
    int: The index of the second largest element in the array.
    """
    max_val = second_max = float('-inf')
    max_index = second_max_index = -1
    
    for i, num in enumerate(arr):
        if num > max_val:
            second_max = max_val
            max_val = num
            second_max_index = max_index
            max_index = i
        elif num > second_max and num != max_val:
            second_max = num
            second_max_index = i
            
    return second_max_index