"""
QUESTION:
Implement a function named `bubble_sort(arr)` that sorts the input list `arr` in ascending order without using any built-in sorting functions or libraries, and with a time complexity of O(n^2) and a space complexity of O(1).
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break
    
    return arr