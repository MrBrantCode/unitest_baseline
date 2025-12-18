"""
QUESTION:
Write a function `find_kth_smallest(arr, k)` to find the kth smallest number in a list of integers `arr`, where `k` is a positive integer less than or equal to the length of `arr`. The function should not use any built-in sorting functions or libraries, and its time complexity should be O(n log n). If `arr` is empty or `k` is out of range, the function should return `None`.
"""

def find_kth_smallest(arr, k):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


    if not arr or k < 1 or k > len(arr):
        return None

    low, high = 0, len(arr) - 1
    while True:
        pivot = partition(arr, low, high)
        if pivot == k - 1:
            return arr[pivot]
        elif pivot > k - 1:
            high = pivot - 1
        else:
            low = pivot + 1