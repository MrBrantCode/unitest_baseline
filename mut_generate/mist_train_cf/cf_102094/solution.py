"""
QUESTION:
Write a function `is_sorted` that checks if a given list of integers is sorted in ascending order. The function should return True if the list is sorted in ascending order, and False otherwise. The time complexity of the function should be O(n log n), and the space complexity should be O(log n).
"""

def is_sorted(arr):
    if len(arr) <= 1:
        return True

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    if not is_sorted(left) or not is_sorted(right):
        return False

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr == sorted(arr)