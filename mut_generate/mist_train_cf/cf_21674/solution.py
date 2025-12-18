"""
QUESTION:
Implement a function called `merge_sort` that takes a list of integers as input and returns the number of swaps performed during the sorting process. The function should sort the input list in ascending order without using any built-in sorting functions, handle duplicate integers, and have a time complexity of O(n log n). The function should also be able to handle large input lists efficiently and should only use constant space.
"""

def merge_sort(arr):
    swaps = 0

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        swaps += merge_sort(left_half)
        swaps += merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                swaps += len(left_half) - i
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return swaps