"""
QUESTION:
Implement a binary search function named "binary_search" that takes a sorted list of elements and a target element as input. The function should return the index of the target element if it exists in the list; otherwise, it should return -1. The function should have a time complexity of O(log n), where n is the number of elements in the list. Note that this function will only work correctly if the input list is sorted in ascending order.
"""

def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1