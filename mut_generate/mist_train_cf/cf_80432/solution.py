"""
QUESTION:
Write a function `merge_arrays(arr1, arr2)` that merges two sorted arrays of integers into a single sorted array without using built-in functions. The function should handle potential edge cases, such as an empty array and negative numbers, and should output the merged array. The time complexity of the merging process should be `O(n+m)`, where `n` and `m` are the lengths of the input arrays.
"""

def merge_arrays(arr1, arr2):
    """
    Merge two sorted arrays of integers into a single sorted array.

    The function handles potential edge cases, such as an empty array and negative numbers.
    The time complexity of the merging process is O(n+m), where n and m are the lengths of the input arrays.

    Parameters:
    arr1 (list): The first sorted array of integers.
    arr2 (list): The second sorted array of integers.

    Returns:
    list: The merged sorted array of integers.
    """

    # handle edge case if any of the arrays is empty
    if len(arr1) == 0:
        return arr2
    elif len(arr2) == 0:
        return arr1

    merged_array = []
    i = 0
    j = 0

    # loop through both arrays and push smaller value first
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # if any elements left in first array push into merged array
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # if any elements left in second array push into merged array
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array