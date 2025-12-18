"""
QUESTION:
Implement a function named `dual_pivot_quick_sort` that takes an array `arr` and two indices `low` and `high` as input, and sorts the subarray `arr[low..high]` in ascending order using the dual pivot quicksort algorithm. The function should have a best and average case time complexity of O(n log n) and should be able to handle arrays with duplicate elements.
"""

def partition(arr, low, high): 
    if arr[low] > arr[high]: 
        arr[low], arr[high] = arr[high], arr[low] 

    pivot1, pivot2 = arr[low], arr[high] 
    i, j, k = low + 1, low + 1, high - 1

    while j <= k:  
        if arr[j] < pivot1: 
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
        elif arr[j] > pivot2: 
            while arr[k] > pivot2 and j < k: 
                k -= 1
            arr[j], arr[k] = arr[k], arr[j] 
            k -= 1
            if arr[j] < pivot1: 
                arr[i], arr[j] = arr[j], arr[i] 
                i += 1
        j += 1

    i -= 1
    k += 1
    arr[low], arr[i] = arr[i], arr[low] 
    arr[high], arr[k] = arr[k], arr[high] 

    return i, k 

def dual_pivot_quick_sort(arr, low, high): 
    if low < high: 
        pivot1, pivot2 = partition(arr, low, high) 
        dual_pivot_quick_sort(arr, low, pivot1 - 1) 
        dual_pivot_quick_sort(arr, pivot1 + 1, pivot2 - 1) 
        dual_pivot_quick_sort(arr, pivot2 + 1, high) 