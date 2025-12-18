"""
QUESTION:
Create a function called merge_sorted_arrays that takes two sorted arrays as input and returns a single sorted array containing all elements from both input arrays. The function should have a time complexity of O(n), where n is the total number of elements in both arrays.
"""

def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into a single sorted array.

    Args:
    arr1 (list): The first sorted array.
    arr2 (list): The second sorted array.

    Returns:
    list: A single sorted array containing all elements from both input arrays.
    """
    merged_array = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    
    return merged_array