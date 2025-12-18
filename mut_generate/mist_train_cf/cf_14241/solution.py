"""
QUESTION:
Implement a function called `merge_sort` that takes a list of integers as input and returns the sorted list in ascending order. The function should have a time complexity of O(nlogn) and use a stable sorting algorithm. The implementation must be from scratch, without using any built-in sorting functions or libraries. The function should work with basic data structures such as arrays or linked lists, but not with advanced data structures such as heaps or binary trees.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    sorted_list = []
    i = j = 0
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            sorted_list.append(sorted_left[i])
            i += 1
        else:
            sorted_list.append(sorted_right[j])
            j += 1
    sorted_list += sorted_left[i:]
    sorted_list += sorted_right[j:]
    return sorted_list