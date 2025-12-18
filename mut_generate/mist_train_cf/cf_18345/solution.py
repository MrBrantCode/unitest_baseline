"""
QUESTION:
Write a function named `find_kth_smallest` that takes a list of integers `arr` and a positive integer `k` as input, where `k` is less than or equal to the length of `arr`. The function should return the kth smallest number in `arr` without using any built-in sorting functions or libraries. The time complexity of the function should be O(n log n).
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def find_kth_smallest(arr, k):
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