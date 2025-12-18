"""
QUESTION:
Create a function `bubble_sort` that takes an array of random integers ranging from 1 to 1000 as input. The size of the array is determined by the user and must be a prime number. The function should sort the array in ascending order using the bubble sort algorithm, and return the sorted array along with the number of swaps performed during the sorting process.
"""

def entrance(arr):
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return arr, swaps