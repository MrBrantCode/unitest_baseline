"""
QUESTION:
Implement the `merge_sort` function to sort a given list of integers in ascending order using the merge sort algorithm. The function should take one argument, a list of integers, and return the sorted list. The function should use a recursive approach to divide the list into two halves until each sublist contains one element or is empty, and then merge the sublists in sorted order.
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
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result