"""
QUESTION:
Write a function `find_kth_smallest` that retrieves the kth smallest element from a given list of integers. The input list may contain duplicate elements and k is an integer between 1 and the length of the list (inclusive). The function should run in O(n) time complexity. If k is out of range, return None.
"""

def find_kth_smallest(arr, k):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_select(arr, low, high, k):
        if low == high:
            return arr[low]
        
        pivot_index = partition(arr, low, high)
        
        if k == pivot_index:
            return arr[pivot_index]
        elif k < pivot_index:
            return quick_select(arr, low, pivot_index - 1, k)
        else:
            return quick_select(arr, pivot_index + 1, high, k)

    if k < 1 or k > len(arr):
        return None
    
    return quick_select(arr, 0, len(arr) - 1, k - 1)