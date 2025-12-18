"""
QUESTION:
Implement a function named `bubble_sort` that takes an array as input and returns the array sorted in ascending order using the bubble sort algorithm. The function should use nested loops to compare and swap elements, without using the built-in sort() or sorted() functions.
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr