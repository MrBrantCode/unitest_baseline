"""
QUESTION:
Implement a function called `merge_sort_descending` that takes a list of integers as input, and returns the list sorted in descending order using recursion, without using any built-in sorting functions or data structures. The function should not have any restrictions on the size of the input list.
"""

def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr

    left_half = arr[:len(arr) // 2]
    right_half = arr[len(arr) // 2:]

    left_half = merge_sort_descending(left_half)
    right_half = merge_sort_descending(right_half)

    merged_list = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] >= right_half[j]:
            merged_list.append(left_half[i])
            i += 1
        else:
            merged_list.append(right_half[j])
            j += 1

    merged_list.extend(left_half[i:])
    merged_list.extend(right_half[j:])

    return merged_list