"""
QUESTION:
Design a function `find_kth_smallest` that takes an array of integers and an integer k as input, and returns the k-th smallest element in the array. The function should have a time complexity of O(n) and space complexity of O(1), and should be able to handle arrays containing duplicates, as well as positive and negative integers. The value of k should be 1-indexed, and the function should return None if k is less than 1 or greater than the length of the array.
"""

def find_kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None

    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickselect(arr, low, high, k):
        if low == high:
            return arr[low]

        pivot_index = partition(arr, low, high)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickselect(arr, low, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, high, k)

    return quickselect(arr, 0, len(arr) - 1, k - 1)