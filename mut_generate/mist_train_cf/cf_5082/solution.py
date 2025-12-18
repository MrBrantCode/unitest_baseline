"""
QUESTION:
Implement a function `merge_sort(arr, ascending)` that takes a list `arr` and a boolean flag `ascending` as input and returns the sorted list. The function should sort the list in ascending order if `ascending` is `True` and in descending order otherwise. The function should have a time complexity of O(n log n) and a space complexity of O(n), where n is the number of elements in the list. The function should be implemented iteratively, without using recursion or built-in sorting functions or libraries, and should preserve the original order of equal elements.
"""

def merge(left, right, ascending):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (left[i] <= right[j] and ascending) or (left[i] >= right[j] and not ascending):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(arr, ascending):
    size = 1
    while size < len(arr):
        i = 0
        while i < len(arr):
            mid = i + size - 1
            j = mid + 1
            end = min(i + 2 * size - 1, len(arr) - 1)
            left = arr[i:mid + 1]
            right = arr[j:end + 1]
            if ascending:
                arr[i:end + 1] = merge(left, right, ascending)
            else:
                arr[i:end + 1] = merge(right, left, ascending)
            i += 2 * size
        size *= 2
    return arr