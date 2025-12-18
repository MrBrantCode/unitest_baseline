"""
QUESTION:
Implement a function `merge_sort` that takes a list of integers as input and returns the sorted list in ascending order. The function should have a time complexity of O(nlogn) and should not use any built-in sorting functions or libraries. The input list can contain duplicate elements and can have a length of at most 10^6.
"""

def entance(my_list):
    if len(my_list) <= 1:
        return my_list
    
    mid = len(my_list) // 2
    left_half = my_list[:mid]
    right_half = my_list[mid:]
    
    left_half = entance(left_half)
    right_half = entance(right_half)
    
    return merge(left_half, right_half)

def merge(left_half, right_half):
    sorted_list = []
    
    while left_half and right_half:
        if left_half[0] <= right_half[0]:
            sorted_list.append(left_half[0])
            left_half = left_half[1:]
        else:
            sorted_list.append(right_half[0])
            right_half = right_half[1:]
    
    if left_half:
        sorted_list.extend(left_half)
    elif right_half:
        sorted_list.extend(right_half)
    
    return sorted_list