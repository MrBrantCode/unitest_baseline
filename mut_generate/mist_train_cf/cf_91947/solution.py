"""
QUESTION:
Write an iterative implementation of the quick_sort function that sorts an array of elements in ascending order using the quicksort algorithm. The function should take an array as input and return the sorted array. The implementation should use a stack to keep track of subarrays to be partitioned and a partition function to rearrange the elements in each subarray.
"""

def entrance(arr):
    stack = [(0, len(arr)-1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1