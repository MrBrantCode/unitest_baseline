"""
QUESTION:
Construct a function named `bubble_sort` that takes a list of integers as input and sorts it in descending order using the bubble sort algorithm. The time complexity of the solution should be O(n^2), where n is the number of elements in the list, and the space complexity should be O(1), meaning no extra data structures should be used.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr