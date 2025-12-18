"""
QUESTION:
Write a function `find_index_recursive` that takes an array of integers `arr`, a target value `target`, and an index `index` as parameters, and returns the index of the first occurrence of the target value in the array without using any looping constructs. If the target value is not found in the array, return -1.
"""

def find_index_recursive(arr, target, index):
    """
    This function returns the index of the first occurrence of the target value in the array.
    
    Parameters:
    arr (list): The input array.
    target (int): The target value to be searched.
    index (int): The current index.
    
    Returns:
    int: The index of the first occurrence of the target value, -1 if not found.
    """
    if index == len(arr) - 1:
        return -1 if arr[index] != target else index
    elif arr[index] == target:
        return index
    else:
        return find_index_recursive(arr, target, index + 1)