"""
QUESTION:
Implement a function called `merge_sort()` that takes a list of integers as input and returns the sorted list in ascending order using a divide and conquer approach with a time complexity of O(n log n). The function should not use any built-in sorting functions or libraries. The input list can be divided into two equal halves, and each half should be recursively sorted and then merged back together.
"""

def merge_sort(arr):
    # Base case: if the list has only one element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the list into two equal halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the first and second halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    left_pointer = 0
    right_pointer = 0
    
    # Compare elements from both halves and add the smaller element to the result list
    while left_pointer < len(left_half) and right_pointer < len(right_half):
        if left_half[left_pointer] <= right_half[right_pointer]:
            result.append(left_half[left_pointer])
            left_pointer += 1
        else:
            result.append(right_half[right_pointer])
            right_pointer += 1
    
    # Add the remaining elements of the first half
    while left_pointer < len(left_half):
        result.append(left_half[left_pointer])
        left_pointer += 1
    
    # Add the remaining elements of the second half
    while right_pointer < len(right_half):
        result.append(right_half[right_pointer])
        right_pointer += 1
    
    return result