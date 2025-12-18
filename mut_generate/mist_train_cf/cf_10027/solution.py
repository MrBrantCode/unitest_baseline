"""
QUESTION:
Implement a function `rotate_list_reverse(lst, k)` that takes a list `lst` and an integer `k` as input. Rotate the list to the right by `k` elements, where the rotation is performed in reverse order. In other words, the last `k` elements of the original list should become the first `k` elements of the rotated list, and the remaining elements should maintain their original order but be shifted to the right. The function should return the rotated list.
"""

def rotate_list_reverse(lst, k):
    # Reverse the entire list
    lst = lst[::-1]
    
    # Reverse the first k elements
    lst[:k] = lst[:k][::-1]
    
    # Reverse the remaining elements after k
    lst[k:] = lst[k:][::-1]
    
    return lst