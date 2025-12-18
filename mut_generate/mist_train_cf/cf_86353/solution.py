"""
QUESTION:
Implement a function `bubble_sort(arr)` that sorts the input array in descending order using the bubble sort algorithm. The function should have a time complexity of O(n^2) and a space complexity of O(1), and it should not use any additional data structures or built-in sorting functions.
"""

def entance(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr