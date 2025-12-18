"""
QUESTION:
Write a function called bubble_sort that sorts an array of integers in descending order using the bubble sort algorithm. The function should not use any additional data structures or built-in sorting functions, and it should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr