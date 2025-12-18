"""
QUESTION:
Implement a function called `bubble_sort_descending` that takes an array of integers as input and returns the array sorted in descending order using the bubble sort algorithm. The input array may contain duplicate values and its size can vary. The function should modify the input array to be sorted in-place.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr