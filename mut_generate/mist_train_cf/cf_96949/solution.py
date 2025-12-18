"""
QUESTION:
Implement a recursive function `sort_list` to sort a list of size n, where n is a positive integer. The function should not use loops or built-in sorting algorithms, and instead, use a helper function `merge` to combine and sort the sub-lists. Analyze the time and space complexity of the `sort_list` function.
"""

def sort_list(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left_half = sort_list(lst[:mid])
    right_half = sort_list(lst[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged