"""
QUESTION:
Implement a Python function named `sort_string` that takes a string input, removes any spaces, and returns the string with its individual characters sorted in descending order using the QuickSort algorithm. The function should not use any built-in sorting functions.
"""

def sort_string(s):
    arr = list(s.replace(" ", ""))
    n = len(arr)
    def partition(arr, low, high):
        i = (low-1)        
        pivot = arr[high]   
        for j in range(low, high):
            if arr[j] >= pivot:
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

    quickSort(arr, 0, n-1)
    return "".join(arr)