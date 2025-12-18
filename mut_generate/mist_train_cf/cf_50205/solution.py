"""
QUESTION:
Write a function called `find_element` that takes in an array and a target value, and returns the index of the target value in the array. If the target value is not found, return a message indicating that the value is not in the array. The function should be able to handle arrays of different data types, including integers and strings.
"""

def find_element(arr, target):
    """
    This function finds the index of the target value in the given array.
    
    Parameters:
    arr (list): The array to search in.
    target: The target value to search for.
    
    Returns:
    int: The index of the target value if found, otherwise a message indicating that the value is not in the array.
    """
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return f"{target} is not in the array."