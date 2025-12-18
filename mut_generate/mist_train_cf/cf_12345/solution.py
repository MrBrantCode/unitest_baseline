"""
QUESTION:
Implement a function `sort_array(arr, N)` that sorts the given list `arr` up to the `N`th element in increasing order. The function should use only constant space complexity, i.e., no additional data structures are allowed.
"""

def sort_array(arr, N):
    for i in range(N):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr