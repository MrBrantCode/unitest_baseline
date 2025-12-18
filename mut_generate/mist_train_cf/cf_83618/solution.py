"""
QUESTION:
Implement a function `bubbleSort(arr)` that takes a list of numbers as input and returns the list in ascending order using the Bubble sort algorithm. The function should handle real numbers and negative values. Ensure the function is correctly implemented to avoid errors and analyze its time complexity.
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr