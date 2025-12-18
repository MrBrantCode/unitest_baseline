"""
QUESTION:
Create a function named `merge_sort` that sorts a list of integers in ascending order using a divide and conquer approach with a time complexity of O(n log n) without using built-in sorting functions or libraries. The function should return the sorted list.

Input: A list of integers
Output: A sorted list of integers in ascending order
Restrictions: The function must have a time complexity of O(n log n) and use a divide and conquer approach without built-in sorting functions or libraries.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left_half, right_half):
    merged_arr = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged_arr.append(left_half[left_index])
            left_index += 1
        else:
            merged_arr.append(right_half[right_index])
            right_index += 1

    while left_index < len(left_half):
        merged_arr.append(left_half[left_index])
        left_index += 1

    while right_index < len(right_half):
        merged_arr.append(right_half[right_index])
        right_index += 1

    return merged_arr