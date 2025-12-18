"""
QUESTION:
Implement a function `merge_sort` that takes an input array `arr`, a starting index `start`, and an ending index `end`. The function should sort the array in increasing order using the merge sort algorithm with a time complexity of O(N log N) and a space complexity of O(N), where N is the size of the array. The function should not use any additional data structures and should be able to handle arrays of size up to 10^5 with maximum values up to 10^5.
"""

def merge_sort(arr, start, end):
    if start >= end:
        return
    
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    left_arr = arr[start:mid+1]
    right_arr = arr[mid+1:end+1]

    i = j = 0
    k = start

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1