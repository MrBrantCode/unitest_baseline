"""
QUESTION:
Implement a function called `merge_sort` that takes a list of integers as input, sorts the list in ascending order using the Merge Sort algorithm, and returns the sorted list. The function should not use any built-in sorting functions or libraries.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    sorted_arr = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1

    while i < len(left_half):
        sorted_arr.append(left_half[i])
        i += 1

    while j < len(right_half):
        sorted_arr.append(right_half[j])
        j += 1

    return sorted_arr