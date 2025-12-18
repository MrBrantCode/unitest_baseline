"""
QUESTION:
Write a function `sort_positive_negative` that takes an array of integers as input and returns the array sorted such that all negative numbers are in descending order, followed by the non-negative numbers in ascending order. The function should be efficient and able to handle arrays with both positive and negative integers.
"""

def sort_positive_negative(array):
    negative = [i for i in array if i < 0]
    positive = [i for i in array if i >= 0]

    def partition(arr, low, high):
        i = (low-1)  
        pivot = arr[high] 
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quickSort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(arr, low, high)
            quickSort(arr, low, pi-1)
            quickSort(arr, pi+1, high)

    quickSort(negative, 0, len(negative)-1)
    quickSort(positive, 0, len(positive)-1)
    
    return negative[::-1] + positive 