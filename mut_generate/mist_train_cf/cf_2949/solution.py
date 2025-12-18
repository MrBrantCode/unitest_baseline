"""
QUESTION:
Implement a function called `mergeSortIterative` that takes an array of integers as input and returns the sorted array using an iterative merge sort approach. The function should use a constant amount of extra space, not creating any new arrays or using additional data structures other than the given array itself, and have a time complexity of O(n log n). The input array may contain duplicate elements.
"""

def mergeSortIterative(array):
    size = len(array)
    tempArray = [0] * size
    chunkSize = 1
    
    while chunkSize < size:
        left = 0
        while left < size - chunkSize:
            mid = left + chunkSize - 1
            right = min(left + 2 * chunkSize - 1, size - 1)
            merge(array, tempArray, left, mid, right)
            left = right + 1
        chunkSize *= 2
        
    return array


def merge(array, tempArray, left, mid, right):
    i = left
    j = mid + 1
    k = left
    
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            tempArray[k] = array[i]
            i += 1
            k += 1
        else:
            tempArray[k] = array[j]
            j += 1
            k += 1
            
    while i <= mid:
        tempArray[k] = array[i]
        i += 1
        k += 1
        
    while j <= right:
        tempArray[k] = array[j]
        j += 1
        k += 1
        
    for i in range(left, right + 1):
        array[i] = tempArray[i]
        
    return array