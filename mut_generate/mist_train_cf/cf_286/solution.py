"""
QUESTION:
Implement a function called `merge_sort` that takes a list of integers as input and returns a new list with the integers sorted in ascending order using the merge sort algorithm, without using any built-in sorting functions or libraries. The input list can be empty, contain duplicate numbers, and contain both positive and negative numbers. The function should have the following signature: `def merge_sort(nums: List[int]) -> List[int]:`
"""

from typing import List

def merge_sort(nums: List[int]) -> List[int]:
    # Base case: if the list is empty or has only one element, it is already sorted
    if len(nums) <= 1:
        return nums
    
    # Divide the list into two halves
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]
    
    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i = j = 0
    
    # Compare the first elements of each half and add the smaller one to the merged list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add the remaining elements from the other half to the merged list
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged