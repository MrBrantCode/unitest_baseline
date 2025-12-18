"""
QUESTION:
Implement a function named `timsort` that sorts the elements of an array using TimSort, an adaptive sorting technique derived from merge sort and insertion sort. The function should be able to sort an array of integers and return the sorted array. The input array can be of any size and contain any integer values.
"""

def timsort(arr):
    min_run = 32
    n = len(arr)

    def insertion_sort(left, right=None):
        if right is None:
            right = len(arr) - 1

        for i in range(left + 1, right + 1):
            key_item = arr[i]
            j = i - 1
            while j >= left and arr[j] > key_item:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key_item

    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])
        return merged

    for i in range(0, n, min_run):
        insertion_sort(i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged = merge(
                left=arr[start:midpoint + 1],
                right=arr[midpoint + 1:end + 1])
            arr[start:start + len(merged)] = merged
        size *= 2

    return arr