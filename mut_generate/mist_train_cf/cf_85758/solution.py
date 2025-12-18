"""
QUESTION:
Create a function named `bubble_sort` that sorts an array in ascending order using the bubble sort algorithm. The function should take an array as input and return the sorted array.
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr