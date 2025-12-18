"""
QUESTION:
Write a function called `sort_negative` that takes a list of integers as input and returns the same list with all negative numbers sorted in ascending order, while keeping the position of non-negative numbers unchanged. The function must implement a sorting algorithm from scratch with a time complexity of O(n^2), without using any built-in sorting functions or libraries, and without using additional data structures or variables to store intermediate results.
"""

def sort_negative(arr):
    n = len(arr)
    for i in range(n):
        min_neg_index = i
        if arr[min_neg_index] >= 0:
            continue  # Skip positive elements
        for j in range(i+1, n):
            if arr[j] < 0 and arr[j] < arr[min_neg_index]:
                min_neg_index = j
        if min_neg_index != i:
            arr[i], arr[min_neg_index] = arr[min_neg_index], arr[i]
    return arr