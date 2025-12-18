"""
QUESTION:
Write a function called `bubble_sort` that takes an array of strings as input and returns the array sorted in descending alphabetical order using the Bubble Sort algorithm.
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr