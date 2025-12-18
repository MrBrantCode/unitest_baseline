"""
QUESTION:
Implement a function named `median` in Python to compute the median of an array containing floating-point numbers without using the built-in sorted() function or any external library. The array may contain up to 1 million elements. The time complexity of your solution should be O(n log n).
"""

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def median(arr):
    quicksort(arr, 0, len(arr) - 1)
    
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]