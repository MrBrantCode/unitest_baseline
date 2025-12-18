"""
QUESTION:
Implement the quicksort algorithm to sort an array of integers in ascending order using the last element as the pivot and without using any built-in sorting functions or libraries. The function should have a time complexity of O(n log n) and a space complexity of O(1). The array can have duplicate numbers and its length should be at least 10.

You are required to implement two functions: `partition` and `quicksort`. The `partition` function should take the array, start index, and end index as parameters, and return the index of the pivot element after partitioning. The `quicksort` function should take the array, start index, and end index as parameters, and call the `partition` function and recursively sort the subarrays.
"""

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
 
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
 
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)