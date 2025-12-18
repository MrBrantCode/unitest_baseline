"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of non-negative integers as input and returns the list sorted in descending order using the bubble sort algorithm. The function should modify the original list by repeatedly swapping adjacent elements if they are in the wrong order.
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr 