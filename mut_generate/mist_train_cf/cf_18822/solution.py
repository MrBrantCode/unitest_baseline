"""
QUESTION:
Implement a function `quicksort(arr, left, right)` that sorts an array of strings in descending alphabetical order. The function should have a time complexity of O(n log n) and a space complexity of O(1). The input parameters are the array `arr` to be sorted and the indices `left` and `right` that define the portion of the array to be sorted.
"""

def quicksort(arr, left, right):
    if left >= right:
        return
    
    pivotIndex = (left + right) // 2
    pivotValue = arr[pivotIndex]
    
    arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]
    
    partitionIndex = left
    
    for i in range(left, right):
        if arr[i] > pivotValue:
            arr[i], arr[partitionIndex] = arr[partitionIndex], arr[i]
            partitionIndex += 1
    
    arr[partitionIndex], arr[right] = arr[right], arr[partitionIndex]
    
    quicksort(arr, left, partitionIndex - 1)
    quicksort(arr, partitionIndex + 1, right)