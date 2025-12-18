"""
QUESTION:
Write a function `bubble_sort_descending` that sorts an array in descending order using the bubble sort algorithm. Implement the swapping logic correctly. The function should take an array of integers as input and return the sorted array. The time complexity of the bubble sort algorithm is O(n^2) and the space complexity is O(1).
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr