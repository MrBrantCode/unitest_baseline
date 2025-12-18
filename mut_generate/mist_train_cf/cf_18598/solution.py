"""
QUESTION:
Implement the quicksort function with the following requirements: 
- The function should sort an array of integers in ascending order without using built-in sorting functions or libraries.
- The function should have a time complexity of O(n log n) and a space complexity of O(1).
- The function should use the last element of the array as the pivot element.
- The function should implement the partitioning step in a separate function that takes the array, start index, and end index as parameters and returns the index of the pivot element after partitioning.
- The function should call the partition function and recursively sort the subarrays.
- The array can have duplicate numbers and its length should be at least 10. 

Implement two functions, partition and quicksort, that meet the above requirements. The partition function should take an array, start index, and end index as parameters and return the index of the pivot element after partitioning. The quicksort function should take an array, start index, and end index as parameters and recursively sort the array using the partition function.
"""

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def entance(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        entance(arr, low, pivot_index - 1)
        entance(arr, pivot_index + 1, high)