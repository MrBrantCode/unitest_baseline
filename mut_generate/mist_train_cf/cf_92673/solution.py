"""
QUESTION:
Implement a function `quicksort(arr)` that sorts an array of integers using the Quicksort algorithm and returns the number of comparisons and swaps performed during the sorting process. The function should sort the array in-place and return the total number of comparisons and swaps as a tuple. The array is not guaranteed to be sorted and may contain duplicate elements. The function should not take any additional arguments other than the input array.
"""

def quicksort(arr):
    comparisons = 0
    swaps = 0
    
    def partition(arr, low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1
    
    def quicksort_helper(arr, low, high):
        nonlocal comparisons, swaps
        if low < high:
            pivot_index = partition(arr, low, high)
            
            quicksort_helper(arr, low, pivot_index - 1)
            quicksort_helper(arr, pivot_index + 1, high)
    
    quicksort_helper(arr, 0, len(arr) - 1)
    return comparisons, swaps