"""
QUESTION:
Implement a function `ternary_search(arr, l, r, x)` that performs a ternary search on an array to find the index of a target element `x`. The array should be sorted, but the function should first check if the array is sorted. If it's not sorted, the function should sort the array without using built-in Python sorting methods before performing the ternary search.
"""

def entrance(arr, l, r, x):
    def is_sorted(arr):
        n = len(arr)
        return all(arr[i] <= arr[i+1] for i in range(n - 1))

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    if not is_sorted(arr):
        arr = bubble_sort(arr)

    if r >= l:
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2

        if arr[mid1] > x:
            return entrance(arr, l, mid1 - 1, x)
        elif arr[mid2] < x:
            return entrance(arr, mid2 + 1, r, x)
        else:
            return entrance(arr, mid1 + 1, mid2 - 1, x)
    else:
        return -1