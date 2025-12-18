"""
QUESTION:
Write a function `bubble_sort(arr)` that sorts an array of strings in descending order using Bubble Sort. The strings in the array can include alphanumeric characters and special characters. The function should consider the ASCII values of these character types during sorting. The input array will be a list of strings.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr