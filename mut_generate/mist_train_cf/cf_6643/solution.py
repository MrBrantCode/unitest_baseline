"""
QUESTION:
Write a function called `merge_sort` that sorts an array of integers in descending order. The function should have a time complexity of O(n log n), be stable, and not use any built-in sorting functions or libraries. Additionally, the function should not use any extra memory apart from the input array itself, and it should not modify the original array.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result