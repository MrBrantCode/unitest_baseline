"""
QUESTION:
Implement a function `merge_sort(arr)` that sorts an array of integers `arr` in descending order with a time complexity of O(n log n) and stability. The function should not use any built-in sorting functions or libraries and should not modify the original array. Additionally, it should not use any extra memory apart from the input array itself.
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