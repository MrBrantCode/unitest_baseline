"""
QUESTION:
Implement a function `find_median` that takes a list of numbers as input, sorts the list in ascending order, and returns the middle element as the median. The input list will always have an odd number of elements. Your implementation should achieve a time complexity of O(nlogn) and a space complexity of O(1) without using any built-in functions or libraries that directly calculate the median.
"""

def find_median(arr):
    def partition(low, high):
        i = (low-1)
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quicksort(low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(low, high)
            quicksort(low, pi-1)
            quicksort(pi+1, high)

    n = len(arr)
    quicksort(0, n-1)
    middle_index = n // 2
    return arr[middle_index]