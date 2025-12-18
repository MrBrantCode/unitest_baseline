"""
QUESTION:
Create a function called `sort_descending` that sorts a given set of integers in descending order. The function should take an array of integers as input and return the sorted array. The function should work for any set of integers, not just the set {1, 2, 3, 4, 5}.
"""

def sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr