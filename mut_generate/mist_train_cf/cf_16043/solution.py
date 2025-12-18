"""
QUESTION:
Write a function `findKthSmallest` that takes an array of integers and an integer `k` as input and returns the kth smallest element in the array. The function must not use any sorting algorithms or built-in functions, and it must only use a constant amount of extra space. The function should run in O(n) time complexity on average.
"""

def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end
    
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[start], arr[j] = arr[j], arr[start]
    return j

def findKthSmallest(arr, k):
    start = 0
    end = len(arr) - 1
    pivotIndex = -1
    
    while pivotIndex != k-1:
        pivotIndex = partition(arr, start, end)
        if pivotIndex < k-1:
            start = pivotIndex + 1
        elif pivotIndex > k-1:
            end = pivotIndex - 1
    
    return arr[pivotIndex]