"""
QUESTION:
Create a function `merge_sort(arr)` that sorts a list of integers in ascending order using a divide and conquer approach with a time complexity of O(n log n) without using any built-in sorting functions or libraries. The function should take a list of integers as input and return the sorted list as output.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
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