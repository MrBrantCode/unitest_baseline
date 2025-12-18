"""
QUESTION:
Implement a function `sort_array(A)` that sorts the input array `A` in ascending order. The function should take a list `A` as input and return the sorted list. The function must use the given pseudocode's algorithm, which involves finding the minimum element in the unsorted part of the array and swapping it with the first element of the unsorted part.
"""

def sort_array(A):
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if A[min_index] > A[j]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A