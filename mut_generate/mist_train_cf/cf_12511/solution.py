"""
QUESTION:
Implement a correct `merge_sort` function that takes an array as input and returns the sorted array using the Merge sort algorithm, which has a time complexity of O(n log n). Note that the `merge` function should be implemented to correctly merge two sorted arrays into one sorted array. Ensure that the `merge_sort` function does not swap the left and right subarrays recursively.
"""

def merge_sort(arr):
    """
    Sorts an array using the Merge sort algorithm.

    Args:
    arr (list): The input array to be sorted.

    Returns:
    list: The sorted array.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted arrays into one sorted array.

    Args:
    left (list): The first sorted array.
    right (list): The second sorted array.

    Returns:
    list: The merged sorted array.
    """
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result