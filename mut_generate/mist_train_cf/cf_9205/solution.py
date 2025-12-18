"""
QUESTION:
Implement the `merge_sort` function to sort a list of integers in ascending order with a time complexity of O(nlogn) without using any built-in sorting functions or libraries. The function should handle lists of length up to 10^6 and correctly sort duplicate elements.
"""

def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    
    mid = len(my_list) // 2
    left_half = my_list[:mid]
    right_half = my_list[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
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