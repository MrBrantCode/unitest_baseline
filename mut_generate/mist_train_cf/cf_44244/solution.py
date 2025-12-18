"""
QUESTION:
Implement a function called `bubble_sort_optimized` that sorts an array of numbers in-place using the bubble sort algorithm and returns a tuple containing the sorted array, the number of iterations, and the number of comparisons made. The function should minimize the number of iterations and comparisons by stopping if no swaps are made in an iteration and reducing the scope of each iteration by excluding previously sorted elements.
"""

def bubble_sort_optimized(arr):
    n = len(arr)
    comparisons = 0
    iterations = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1): 
            comparisons += 1
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        iterations += 1
        if swapped == False:
            break
    return arr, iterations, comparisons