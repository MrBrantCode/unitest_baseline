"""
QUESTION:
Create a function called `create_sorted_lists` that takes a list of elements as input and returns two lists containing the same elements in the same order, with a time complexity of O(n log n).
"""

def create_sorted_lists(arr):
    if len(arr) <= 1:
        return [arr, arr]
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half, _ = create_sorted_lists(left_half)
    right_half, _ = create_sorted_lists(right_half)
    
    return merge(left_half, right_half), merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    i = 0
    j = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    
    return result