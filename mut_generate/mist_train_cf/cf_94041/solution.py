"""
QUESTION:
Create a function named `sort_2d_list` that takes a 2D list as input and returns a new sorted 2D list based on the second element of each sublist. The function should handle cases where the second element is a string, negative number, float, or tuple, assigning a higher value to strings and a lower value to tuples. The function should have a time complexity of O(n log n) and should not use any built-in Python sorting functions.
"""

def sort_2d_list(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left_half = sort_2d_list(lst[:mid])
    right_half = sort_2d_list(lst[mid:])
    
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        left_item = left[left_index]
        right_item = right[right_index]
        
        if isinstance(left_item[1], (int, float)):
            left_value = left_item[1]
        elif isinstance(left_item[1], str):
            left_value = float('inf')
        else:
            left_value = 0
        
        if isinstance(right_item[1], (int, float)):
            right_value = right_item[1]
        elif isinstance(right_item[1], str):
            right_value = float('inf')
        else:
            right_value = 0
        
        if left_value < right_value:
            merged.append(left_item)
            left_index += 1
        else:
            merged.append(right_item)
            right_index += 1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged