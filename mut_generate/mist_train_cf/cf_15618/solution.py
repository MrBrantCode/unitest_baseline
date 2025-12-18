"""
QUESTION:
Implement a function `merge_sort` that takes an array of integers as input and returns the sorted array using a modified merge sort algorithm. The algorithm should use a binary search to find the correct position for each element in the sorted subarray during the merge process. The function should be able to handle arrays of any size and should not have any additional space complexity restrictions.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            # Find the correct position for right[j] in the sorted subarray left[i:]
            pos = binary_search(left, right[j], i)
            result.extend(left[i:pos])
            result.append(right[j])
            i = pos
            j += 1

    # Append the remaining elements from either left or right
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def binary_search(arr, target, start):
    low = start
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low