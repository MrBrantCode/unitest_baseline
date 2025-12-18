"""
QUESTION:
Implement the `bubbleSortDescending` function to sort a given array of integers in descending order using a variation of the bubble sort algorithm with a time complexity of O(n^2). The function should take an array of integers as input, handle arrays with up to 100,000 elements, and return the sorted array.
"""

def bubbleSortDescending(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        length -= 1
    return arr