"""
QUESTION:
Merge two sorted arrays into one sorted array in linear time. Implement a function `merge_sorted_arrays` that takes two sorted arrays as input and returns a new sorted array containing all elements from both arrays. The function must have a time complexity of O(n), where n is the total number of elements in both arrays.
"""

def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into one sorted array in linear time.

    Args:
        arr1 (list): The first sorted array.
        arr2 (list): The second sorted array.

    Returns:
        list: A new sorted array containing all elements from both arrays.
    """
    result = []
    i, j = 0, 0

    # Merge smaller elements first
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # If there are remaining elements in arr1, append them to the result
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # If there are remaining elements in arr2, append them to the result
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result