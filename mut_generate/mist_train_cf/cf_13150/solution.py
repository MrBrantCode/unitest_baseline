"""
QUESTION:
Write a function named `quicksort(arr)` that sorts the input array in ascending order using the Quicksort algorithm and returns the total number of comparisons and swaps performed during the sorting process. The function should modify the input array in place.
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