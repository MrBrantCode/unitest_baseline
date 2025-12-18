"""
QUESTION:
Write a function named `find_kth_smallest` that finds the Kth smallest element in an array of N elements using a recursive algorithm with a time complexity of O(NlogN). The function should not use any sorting algorithms or built-in functions for sorting. The input array is not sorted, and the value of K is in the range 1 to N. The function should return the Kth smallest element if it exists, otherwise return None.
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