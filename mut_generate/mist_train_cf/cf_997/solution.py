"""
QUESTION:
Implement a function `sortArray(arr)` that takes an array of integers as input, sorts the elements in descending order, and returns the sorted array. The function should not use any built-in sorting functions or libraries, and should have a time complexity of O(nlogn), where n is the number of elements in the array. Additionally, the function should sort the elements in-place, directly modifying the original array, and should be a stable sorting algorithm, maintaining the relative order of equal elements.
"""

def sortArray(arr):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        
        while i <= j:
            while i <= j and arr[i] >= pivot:
                i += 1
            while i <= j and arr[j] <= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quickSort(arr, low, high):
        if low >= high:
            return
        
        pivotIndex = partition(arr, low, high)
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)

    quickSort(arr, 0, len(arr) - 1)
    arr.reverse()