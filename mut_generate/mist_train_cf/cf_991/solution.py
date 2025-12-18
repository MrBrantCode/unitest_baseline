"""
QUESTION:
Create a function called `sort_list` that sorts a list of integers in ascending order using a divide and conquer approach. The function should have a time complexity of O(n^2), should not use any built-in sorting functions or data structures, and should handle duplicate integers and negative integers correctly. The input list will contain up to 1,000,000 integers ranging from -10,000,000 to 10,000,000.
"""

def sort_list(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = sort_list(nums[:mid])
    right = sort_list(nums[mid:])
    
    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged