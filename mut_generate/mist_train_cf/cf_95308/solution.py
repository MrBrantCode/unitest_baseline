"""
QUESTION:
Write a function `find_kth_smallest` that takes an array of integers `arr` and an integer `k` as input, and returns the Kth smallest element from the array. The function should use a recursive algorithm and have a time complexity of O(NlogN). It should not use any sorting algorithms or built-in functions for sorting. The function should return `None` if `k` is less than 1 or greater than the length of the array. The array index is 0-based, so the first element is the 1st smallest element, and `k` should be adjusted accordingly.
"""

def find_kth_smallest(arr, k):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        
        while True:
            while i <= j and arr[i] < pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        
        arr[low], arr[j] = arr[j], arr[low]
        
        return j

    def kth_smallest(arr, low, high, k):
        if low == high:
            return arr[low]
        
        pivot_index = partition(arr, low, high)
        
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return kth_smallest(arr, low, pivot_index - 1, k)
        else:
            return kth_smallest(arr, pivot_index + 1, high, k)

    if k < 1 or k > len(arr):
        return None
    
    return kth_smallest(arr, 0, len(arr) - 1, k - 1)