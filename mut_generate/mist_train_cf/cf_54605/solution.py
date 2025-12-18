"""
QUESTION:
Write a function `find_median` that takes an array of integers as input and returns the median value of the array. The function should first sort the array using a sorting algorithm implemented from scratch, such as bubble sort. The array consists of integers in the inclusive range of -10^6 to 10^6.
"""

# This is a simple implementation of the bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

def find_median(arr):
    arr = bubble_sort(arr) # First we sort the array
    n = len(arr)
    median = 0
    
    # if the length of the array is even
    if n % 2 == 0:
        median = (arr[n//2] + arr[n//2 - 1]) / 2
    # if the length of the array is odd
    else:
        median = arr[n//2]
    
    return median