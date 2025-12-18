"""
QUESTION:
Create a function called `merge_sort` that takes a list of numbers as input, sorts them in ascending order using the merge sort algorithm, and returns the sorted list. The input list can be of any length and may contain duplicate numbers. The function should divide the input list into two halves, recursively sort each half, and merge the sorted halves back together.
"""

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])
    
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged