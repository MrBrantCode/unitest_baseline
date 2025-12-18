"""
QUESTION:
Implement a function called merge_sort(lst) that sorts a list of numbers in ascending order, preserving the relative order of duplicate numbers, without using built-in sorting functions or libraries, and achieving a time complexity of O(n log n). The input list may contain duplicate numbers.
"""

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    sorted_lst = []
    left_ptr = right_ptr = 0
    
    while left_ptr < len(left_half) and right_ptr < len(right_half):
        if left_half[left_ptr] <= right_half[right_ptr]:
            sorted_lst.append(left_half[left_ptr])
            left_ptr += 1
        else:
            sorted_lst.append(right_half[right_ptr])
            right_ptr += 1
    
    sorted_lst.extend(left_half[left_ptr:])
    sorted_lst.extend(right_half[right_ptr:])
    
    return sorted_lst