"""
QUESTION:
Implement the `selection_sort` function to sort an input array in descending order using the Selection Sort algorithm. The function should not use any built-in sorting functions or methods. The input and output will be lists of integers.
"""

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    
    return arr