"""
QUESTION:
Write a function called `remove_duplicates` that takes a list of numbers as input, sorts the list in ascending order without using any built-in sorting functions or libraries, removes any duplicates from the sorted list, and returns the result. The function should have a time complexity of O(n log n).
"""

def remove_duplicates(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = remove_duplicates(left_half)
    right_half = remove_duplicates(right_half)

    return merge(left_half, right_half)

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

    result = []
    for i in range(len(merged)):
        if i == 0 or merged[i] != merged[i-1]:
            result.append(merged[i])
    return result