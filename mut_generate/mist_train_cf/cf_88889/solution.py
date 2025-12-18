"""
QUESTION:
Design a function named `min_absolute_difference` that takes two lists of integers, `list1` and `list2`, as parameters and returns the minimum absolute difference between two elements of the two lists. The function must have a time complexity of O(nlogn), where n is the total number of elements in both lists combined, and must not use any built-in sorting algorithms or functions.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
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

def min_absolute_difference(list1, list2):
    merged_list = list1 + list2
    sorted_list = merge_sort(merged_list)
    
    min_diff = float('inf')
    for i in range(len(sorted_list) - 1):
        diff = abs(sorted_list[i] - sorted_list[i+1])
        min_diff = min(min_diff, diff)
    
    return min_diff