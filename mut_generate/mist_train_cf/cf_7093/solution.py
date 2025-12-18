"""
QUESTION:
Implement a function named `quicksort` that takes a list `arr` and recursively sorts it in descending order without using any built-in sorting functions or libraries. The function should use the `partition` function to rearrange the list. The `partition` function should take `arr`, `low`, and `high` as parameters, partition the list around a pivot, and return the index of the pivot after partitioning. 

The `quicksort` function should sort the sublists on either side of the pivot in descending order. The function calls should be `quicksort(arr, low, high)`, `quicksort(arr, low, pivot_index - 1)`, and `quicksort(arr, pivot_index + 1, high)`, where `pivot_index` is the return value of the `partition` function.
"""

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] >= pivot:
            i += 1
        while i <= j and arr[j] <= pivot:
            j -= 1
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    
    return j

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)