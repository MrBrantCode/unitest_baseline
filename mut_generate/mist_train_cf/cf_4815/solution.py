"""
QUESTION:
Implement a function named `merge_sort` that takes a list of integers as input and returns a new list with the same integers in ascending order. The function should use a divide and conquer approach with a time complexity of O(n log n) and should not use any built-in sorting functions or libraries.
"""

def entance(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = entance(arr[:mid])
    right_half = entance(arr[mid:])
    
    sorted_arr = []
    left_pointer = 0
    right_pointer = 0
    
    while left_pointer < len(left_half) and right_pointer < len(right_half):
        if left_half[left_pointer] < right_half[right_pointer]:
            sorted_arr.append(left_half[left_pointer])
            left_pointer += 1
        else:
            sorted_arr.append(right_half[right_pointer])
            right_pointer += 1
    
    sorted_arr += left_half[left_pointer:]
    sorted_arr += right_half[right_pointer:]
    
    return sorted_arr