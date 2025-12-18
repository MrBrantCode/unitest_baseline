"""
QUESTION:
Create a function called `bubble_sort` that takes an array of distinct integers as input and returns the sorted array in ascending order. The input array will have at least 2 numbers and at most 10^6 numbers, with values ranging from -10^9 to 10^9. You are not allowed to use any built-in sorting functions or libraries.
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr