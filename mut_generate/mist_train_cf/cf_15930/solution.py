"""
QUESTION:
Implement a function called `bubble_sort` that takes an array of integers as input and returns the sorted array using the bubble sort algorithm. The function should not use any built-in sorting methods or libraries, and it should optimize the algorithm by stopping early if the array becomes sorted before the last iteration.
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