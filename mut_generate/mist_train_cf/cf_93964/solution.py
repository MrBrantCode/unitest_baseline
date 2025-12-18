"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array of integers in descending order using the bubble sort algorithm. The function should have a time complexity of O(n^2) in the worst case and a space complexity of O(1). It should not use any built-in sorting functions or libraries.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr