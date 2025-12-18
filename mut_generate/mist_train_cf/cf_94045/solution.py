"""
QUESTION:
Write a function `findKthSmallest` that finds the kth smallest element in an array of integers. The function should have two parameters: `arr` (the input array) and `k` (the index of the desired smallest element, 1-indexed). The function should return the kth smallest element in the array. 

The function must have the following restrictions: 

- It must not use any sorting algorithms or built-in sorting functions. 
- It must use only a constant amount of extra space (i.e., it cannot create a new array or data structure that scales with the input size).
- It must have an average time complexity of O(n), where n is the number of elements in the array.
"""

def findKthSmallest(arr, k):
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