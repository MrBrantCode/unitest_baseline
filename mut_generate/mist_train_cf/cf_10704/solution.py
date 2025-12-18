"""
QUESTION:
Implement the bubbleSort function to sort an array of numbers from lowest to highest using a sorting algorithm with a time complexity of O(n^2). The array may contain duplicate numbers and has a maximum length of 1000.
"""

def entrance(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr