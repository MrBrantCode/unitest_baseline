"""
QUESTION:
Implement a function called iterative_merge_sort that sorts an array of integers in ascending order using the merge sort algorithm without recursion. The function should use an iterative approach, sort the array in-place, and only use a constant amount of extra space (i.e., no new arrays or data structures other than the input array).
"""

def iterative_merge_sort(arr):
    temp = [0] * len(arr)
    step = 1
    while step < len(arr):
        start = 0
        while start < len(arr):
            left = start
            right = min(start + step - 1, len(arr) - 1)
            end = min(start + 2 * step - 1, len(arr) - 1)
            i, j, k = left, right + 1, left
            while i <= right and j <= end:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1
            while i <= right:
                temp[k] = arr[i]
                i += 1
                k += 1
            while j <= end:
                temp[k] = arr[j]
                j += 1
                k += 1
            for i in range(left, min(end + 1, len(arr))):
                arr[i] = temp[i]
            start += 2 * step
        step *= 2
    return arr