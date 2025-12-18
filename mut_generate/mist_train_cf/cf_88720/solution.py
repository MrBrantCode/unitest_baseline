"""
QUESTION:
Implement a function named `find_median` that calculates the median of an array of numbers without using any built-in sorting functions or libraries. The function should be able to handle arrays with both odd and even numbers of elements, as well as arrays containing duplicates, negative numbers, and floating-point numbers. The time complexity of the algorithm should be O(nlogn), where n is the number of elements in the array.
"""

def find_median(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    def quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi-1)
            quicksort(arr, pi+1, high)

    quicksort(arr, 0, len(arr)-1)
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]