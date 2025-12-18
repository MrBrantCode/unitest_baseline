"""
QUESTION:
Create a function called `sort_array` that takes an array of integers as input. The function should sort the integers in descending order and print the sorted array without using any loops, recursion, built-in sorting functions, or libraries. The function should have a time complexity of O(n log n) or better.
"""

def sort_array(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = sort_array(arr[:mid])
    right_half = sort_array(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged