"""
QUESTION:
Implement the function `bubbleSortDescending(arr)` that sorts the input array of positive integers in descending order using the Bubble Sort Algorithm. The function should handle edge cases such as an empty array or an array with duplicate elements and minimize unnecessary swaps.
"""

def bubbleSortDescending(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr