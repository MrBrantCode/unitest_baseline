"""
QUESTION:
Implement a function named `bubble_sort_descending` that sorts a list of integers in descending order without using any built-in sorting functions or methods. The function should take one argument, `arr`, which is the list of integers to be sorted. The function should return the sorted list. The function should not use any external libraries or built-in sorting functions.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr