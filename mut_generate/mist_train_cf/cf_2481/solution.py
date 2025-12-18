"""
QUESTION:
Create a function `changeCount` that takes two arrays of integers as input and returns the minimum number of changes required to transform the first array into the second array. A change is defined as modifying an element in the first array to match the corresponding element in the second array. The function should return -1 if the input arrays have different lengths. The time complexity of the function should be O(n), where n is the length of the input arrays.
"""

def changeCount(arr1, arr2):
    """
    This function calculates the minimum number of changes required to transform the first array into the second array.
    
    Args:
        arr1 (list): The initial array of integers.
        arr2 (list): The target array of integers.
    
    Returns:
        int: The minimum number of changes required. Returns -1 if the input arrays have different lengths.
    """
    if len(arr1) != len(arr2):
        return -1
    
    count = 0
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            count += 1
    
    return count