"""
QUESTION:
Implement a function named `bubble_sort_descending` that sorts a list of floats in descending order using the bubble sort algorithm. The function should not use any built-in sorting functions or libraries. Additionally, the algorithm should terminate after a maximum of 100 iterations, regardless of the size of the input list.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    iterations = min(n, 100)  # Limiting the maximum iterations to 100

    for i in range(iterations):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr