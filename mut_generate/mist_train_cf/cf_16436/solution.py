"""
QUESTION:
Implement a function `remove_duplicates` that takes a list of numbers as input and returns a sorted list with no duplicates. The function should have a time complexity of O(n log n) and should not use any built-in sorting functions or libraries. The function should handle duplicate numbers in the input list and remove any duplicates from the sorted list that is returned.
"""

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        elif left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def remove_duplicates(arr):
    sorted_arr = merge_sort(arr)
    result = []
    for i in range(len(sorted_arr)):
        if i == 0 or sorted_arr[i] != sorted_arr[i-1]:
            result.append(sorted_arr[i])
    return result