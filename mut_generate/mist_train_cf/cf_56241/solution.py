"""
QUESTION:
Implement a function called `quick_sort_deque` that sorts a double-ended queue (deque) in ascending order using the QuickSort algorithm. The function should take a deque as input, sort it, and return the sorted deque. The function should have a time complexity of O(n log n) in the best and average case and O(n^2) in the worst case.
"""

from collections import deque

def quick_sort_deque(deq):
    arr = list(deq)
    n = len(arr)

    def partition(arr, low, high):
        i = low - 1  
        pivot = arr[high]  
        for j in range(low , high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def quick_sort(arr, low, high):
        if low < high:
            pri_index = partition(arr, low, high)
            quick_sort(arr, low, pri_index-1)
            quick_sort(arr, pri_index+1, high)

    quick_sort(arr, 0, n-1)
    return deque(arr)