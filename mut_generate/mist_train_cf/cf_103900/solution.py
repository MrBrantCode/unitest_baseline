"""
QUESTION:
Create a function `arrayCompare(arr1, arr2)` that takes two arrays `arr1` and `arr2` as input and returns `True` if they are equal and `False` otherwise. The function should not use any built-in comparison functions that directly compare arrays or lists. The function should be able to handle arrays of any length.
"""

def arrayCompare(arr1, arr2):
    """
    This function compares two arrays and returns True if they are equal, False otherwise.
    
    Args:
        arr1 (list): The first array for comparison.
        arr2 (list): The second array for comparison.
    
    Returns:
        bool: True if the arrays are equal, False otherwise.
    """
    
    # Check if the arrays have the same length
    if len(arr1) != len(arr2):
        return False
    
    # Iterate through each element of the arrays
    for i in range(len(arr1)):
        # Compare the elements at the same index
        if arr1[i] != arr2[i]:
            return False
            
    # If all elements are equal, return True
    return True