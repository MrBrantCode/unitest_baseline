"""
QUESTION:
Implement a function called `merge_sort` that takes an array of integers as input and returns the sorted array. The function should use a bottom-up approach without recursion, with a time complexity of O(n log n) and a space complexity of O(n).
"""

def merge_sort(arr):
    n = len(arr)
    temp_arr = [0] * n
    sublist_size = 1
    while sublist_size < n:
        left = 0
        while left < n - 1:
            mid = min(left + sublist_size - 1, n - 1)
            right = min(left + 2 * sublist_size - 1, n - 1)
            merge(arr, temp_arr, left, mid, right)
            left += 2 * sublist_size
        sublist_size *= 2
    return arr

def merge(arr, temp_arr, left, mid, right):
    for i in range(left, right + 1):
        temp_arr[i] = arr[i]
    i = left
    j = mid + 1
    k = left
    while i <= mid and j <= right:
        if temp_arr[i] <= temp_arr[j]:
            arr[k] = temp_arr[i]
            i += 1
        else:
            arr[k] = temp_arr[j]
            j += 1
        k += 1
    while i <= mid:
        arr[k] = temp_arr[i]
        i += 1
        k += 1
    while j <= right:
        arr[k] = temp_arr[j]
        j += 1
        k += 1