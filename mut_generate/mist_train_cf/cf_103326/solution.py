"""
QUESTION:
Implement a function `bubble_sort(arr)` that takes a list of integers as input and returns the list sorted in ascending order using the bubble sort algorithm. The function should modify the original list and return the sorted list without any additional input parameters.
"""

def entance(arr):
    n = len(arr)
    
    for i in range(n-1):
        # Each iteration moves the largest element to the end of the array
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr