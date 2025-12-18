"""
QUESTION:
Implement the `bubbleSortDescending` function to sort an array of positive integers in descending order using the Bubble Sort Algorithm. The function should take an array as input, sort it in descending order, and return the sorted array. The array will only contain positive integers.
"""

def bubbleSortDescending(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr