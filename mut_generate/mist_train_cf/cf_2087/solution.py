"""
QUESTION:
Implement a function `sort_array_descending(arr)` that sorts an array of numbers in descending order. The array may contain both positive and negative numbers, as well as floating-point numbers. The function must be implemented using a single loop and without using any built-in sorting algorithms or libraries. The time complexity of the function should be O(n^2), where n is the length of the input array.
"""

def sort_array_descending(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr