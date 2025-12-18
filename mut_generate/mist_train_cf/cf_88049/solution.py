"""
QUESTION:
Write a function named `sort_negative` that takes a list of integers as input and returns the list with all negative numbers sorted in ascending order. The function must implement a sorting algorithm without using any built-in sorting functions or libraries, and should not use any additional data structures or variables to store intermediate results. The time complexity of the function should be O(n^2).
"""

def sort_negative(arr):
    n = len(arr)
    for i in range(n):
        min_neg_index = i
        if arr[min_neg_index] >= 0:
            continue  
        for j in range(i+1, n):
            if arr[j] < 0 and arr[j] < arr[min_neg_index]:
                min_neg_index = j
        if min_neg_index != i:
            arr[i], arr[min_neg_index] = arr[min_neg_index], arr[i]
    return arr