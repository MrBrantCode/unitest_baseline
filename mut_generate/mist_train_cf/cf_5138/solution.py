"""
QUESTION:
Implement the function `sort_list(arr)` to sort the given list `arr` in descending order using only bitwise operations. The list may contain duplicate elements and negative numbers, and all elements, including duplicates, should be included in the sorted list.
"""

def sort_list(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                arr[i] ^= arr[j]
                arr[j] ^= arr[i]
                arr[i] ^= arr[j]
    return arr