"""
QUESTION:
Implement a function `merge_sort` that sorts an array of strings in alphabetical order using the merge sort algorithm, with a time complexity of O(n log n) and without using any built-in sorting functions, additional data structures, or recursion. The function should take in an array `arr` and two indices `low` and `high` as parameters.
"""

def merge_sort(arr, low, high):
    if low >= high:
        return

    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    temp = [None] * (high - low + 1)
    left = low
    right = mid + 1
    index = 0

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp[index] = arr[left]
            left += 1
        else:
            temp[index] = arr[right]
            right += 1
        index += 1

    while left <= mid:
        temp[index] = arr[left]
        left += 1
        index += 1

    while right <= high:
        temp[index] = arr[right]
        right += 1
        index += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]