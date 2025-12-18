"""
QUESTION:
Implement the `bubble_sort` function that sorts a list of elements in ascending order using the bubble sort algorithm. The function should take a list `arr` as input, and return the sorted list. Optimize the function to reduce the number of iterations in the inner loop by considering the number of iterations already completed in the outer loop.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr