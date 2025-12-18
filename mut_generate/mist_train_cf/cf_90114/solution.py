"""
QUESTION:
Implement a function named `merge_and_sort` that takes two lists `list1` and `list2` as input, merges them, and returns the merged list sorted in ascending order. The function should not use any built-in sorting functions or libraries and should have a time complexity of O(nlogn), where n is the total number of elements in both lists. The function should also handle duplicates and maintain their original order, and use as little extra space as possible.
"""

def merge_sort(arr):
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

def merge_and_sort(list1, list2):
    merged_list = list1 + list2
    return merge_sort(merged_list)