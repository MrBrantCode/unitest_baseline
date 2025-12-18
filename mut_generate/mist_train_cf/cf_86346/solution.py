"""
QUESTION:
Implement the function "merge_sort" that takes a list of numbers as input and returns the sorted list in ascending order. The function should have a time complexity of O(n log n), handle duplicate numbers, and preserve their relative order. The implementation should be space efficient, using only a constant amount of additional memory, and not create any new data structures except for basic data structures. Do not use any built-in sorting functions or libraries.
"""

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    i = j = k = 0
    merged_lst = []

    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            merged_lst.append(sorted_left[i])
            i += 1
        else:
            merged_lst.append(sorted_right[j])
            j += 1
        k += 1

    merged_lst.extend(sorted_left[i:])
    merged_lst.extend(sorted_right[j:])

    return merged_lst