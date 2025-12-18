"""
QUESTION:
Implement a function `merge_sort` to sort an array of strings in descending order based on the length of each string. The function should have a time complexity of O(nlogn) and should not use any built-in sorting functions or libraries. The function should return the sorted array.
"""

def merge_sort(arr):
    """
    Sorts an array of strings in descending order based on the length of each string.

    Args:
    arr (list): The input array of strings.

    Returns:
    list: The sorted array of strings.

    Time complexity: O(nlogn)
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
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if len(left[i]) >= len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
        
    while j < len(right):
        result.append(right[j])
        j += 1
        
    return result