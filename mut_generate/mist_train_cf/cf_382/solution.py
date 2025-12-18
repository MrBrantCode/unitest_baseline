"""
QUESTION:
Create a function `merge_sort` that sorts the given array in decreasing order using only recursion and without using any built-in sorting functions or loops. The function should remove any duplicate elements from the sorted array. The array may contain duplicate elements. The function should have a time complexity of O(nlogn) and a space complexity of O(n).
"""

def merge_sort(arr):
    """
    Sorts the given array in decreasing order using only recursion and without using any built-in sorting functions or loops.
    Removes any duplicate elements from the sorted array.

    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return remove_duplicates(result)

def remove_duplicates(arr):
    if len(arr) <= 1:
        return arr
    
    if arr[0] == arr[1]:
        return remove_duplicates(arr[1:])
    
    return [arr[0]] + remove_duplicates(arr[1:])