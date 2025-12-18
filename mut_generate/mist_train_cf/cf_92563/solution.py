"""
QUESTION:
Write a function named `find_kth_largest` that takes an unsorted list of integers and an integer k as input, and returns the kth largest element in the list. The function should not sort the entire list. Instead, implement a variation of the quickselect algorithm with an average time complexity of O(n), where n is the length of the list.
"""

def find_kth_largest(arr, k):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickselect(arr, low, high, k):
        if low == high:
            return arr[low]
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)

    n = len(arr)
    return quickselect(arr, 0, n - 1, k - 1)