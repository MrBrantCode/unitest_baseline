"""
QUESTION:
Write a function `sort_2d_list` to sort a 2-dimensional list of sublists based on the values of the second element in each sublist. The second element can be an integer, float, string, or tuple. The function should not use any built-in Python sorting functions and have a time complexity of O(n log n). The strings and tuples should be treated as larger than numbers, and the order of equal elements should be maintained.
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
        
        if left_value <= right_value:
            merged.append(left_item)
            left_index += 1
        else:
            merged.append(right_item)
            right_index += 1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged