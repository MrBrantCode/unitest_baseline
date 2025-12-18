"""
QUESTION:
Write a function `find_indices` that takes an array of integers and a target value as input. Return the indices of all occurrences of the target value in the array. If the target value is not found, return an empty array. The time complexity of the function should be O(n), where n is the length of the array.
"""

def find_indices(array, target):
    """
    Returns the indices of all occurrences of the target value in the array.
    
    Args:
        array (list): A list of integers.
        target (int): The target value to be searched.
    
    Returns:
        list: A list of indices where the target value is found. If not found, returns an empty list.
    """
    indices = [i for i, num in enumerate(array) if num == target]
    return indices