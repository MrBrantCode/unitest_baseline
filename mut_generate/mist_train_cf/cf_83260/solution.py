"""
QUESTION:
Implement a function named `merge_sort` that takes a list of tuples with varying lengths as input and returns a new list with the tuples sorted in ascending order based on their summation. The tuples can contain any number of elements. The function should have a time complexity of O(n log n), where n is the number of tuples in the list.
"""

def merge_sort(lst):
    if len(lst) <= 1:  
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if sum(left[left_index]) <= sum(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged