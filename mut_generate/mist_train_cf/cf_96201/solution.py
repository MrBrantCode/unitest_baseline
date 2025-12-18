"""
QUESTION:
Implement a function `bubble_sort(arr)` that takes an array of strings as input and returns the array sorted in descending order using the recursive bubble sort algorithm. The sorted array should have all duplicates grouped together. Note that the input array may contain duplicate strings.
"""

def bubble_sort(arr):
    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1]:
                return False
        return True

    if is_sorted(arr):
        return arr
    else:
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        return bubble_sort(arr)