"""
QUESTION:
Implement a function `custom_sort(arr)` that takes an array of numbers as input and returns the array sorted in descending order. The function should use a custom sorting algorithm with a time complexity of O(n^2) and a space complexity of O(1), without using any external libraries or built-in sorting functions.
"""

def custom_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr