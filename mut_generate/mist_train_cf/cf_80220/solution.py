"""
QUESTION:
Implement a function called `quicksort` that sorts a given list of integers in ascending order using the quicksort algorithm. The function should have a time complexity of O(n log n) on average, where n is the number of elements in the list, and should be an in-place sorting algorithm, meaning it does not require any additional storage.
"""

def quicksort(arr):
    def partition(arr, low, high):
        i = (low-1) 
        pivot = arr[high] 
        for j in range(low, high):
            if arr[j] < pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quicksort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort_helper(arr, low, pi-1)
            quicksort_helper(arr, pi+1, high)

    quicksort_helper(arr, 0, len(arr) - 1)