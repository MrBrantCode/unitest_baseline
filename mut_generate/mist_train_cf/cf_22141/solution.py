"""
QUESTION:
Implement a function called `sort_list` that takes a list as input and returns a sorted list. The function must use recursion to sort the list and should not use any loops or built-in sorting algorithms. The function should have a time complexity of O(n log n) and space complexity of O(n).
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