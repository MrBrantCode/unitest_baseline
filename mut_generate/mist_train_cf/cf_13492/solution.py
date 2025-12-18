"""
QUESTION:
Create a function named 'sum_corresponding_elements' that takes two arrays of integers as input and returns a new array containing the sum of corresponding elements. The function should handle arrays of different lengths by appending the remaining elements of the longer array to the new array.
"""

def sum_corresponding_elements(arr1, arr2):
    """
    This function takes two arrays of integers as input and returns a new array containing 
    the sum of corresponding elements. The function handles arrays of different lengths by 
    appending the remaining elements of the longer array to the new array.
    
    Args:
    arr1 (list): The first array of integers.
    arr2 (list): The second array of integers.
    
    Returns:
    list: A new array containing the sum of corresponding elements.
    """
    new_array = []
    min_length = min(len(arr1), len(arr2))
    max_length = max(len(arr1), len(arr2))

    for i in range(min_length):
        new_array.append(arr1[i] + arr2[i])

    if len(arr1) > len(arr2):
        new_array.extend(arr1[min_length:])
    elif len(arr2) > len(arr1):
        new_array.extend(arr2[min_length:])

    return new_array