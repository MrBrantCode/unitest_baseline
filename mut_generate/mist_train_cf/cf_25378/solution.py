"""
QUESTION:
Find the common elements in two sorted arrays.

Write a function `common_elements` that takes two sorted arrays as input and returns a list of elements that exist in both arrays.

The function should have the following signature: `common_elements(arr1, arr2)`

Note: The input arrays are sorted in ascending order.
"""

def common_elements(arr1, arr2):
    """
    This function takes two sorted arrays as input and returns a list of elements that exist in both arrays.

    Parameters:
    arr1 (list): The first sorted array.
    arr2 (list): The second sorted array.

    Returns:
    list: A list of elements that exist in both arrays.
    """
    i, j = 0, 0
    common = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            common.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
            
    return common