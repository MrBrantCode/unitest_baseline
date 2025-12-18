"""
QUESTION:
Create a function `rearrange` that takes a list of distinct integers as input and returns a list containing a tuple of two indices. The first index is the largest index `i` such that `arr[i]` is not less than `arr[i + 1]`, and the second index is the smallest index `j` greater than `i` such that `arr[j]` is greater than `arr[i]`. If no such indices exist, return `[(index: -1, swap_with: -1)]`.
"""

def rearrange(arr):
    size = len(arr)
    index = -1
    for i in range(size - 1):
        if arr[i] < arr[i + 1]:
            index = i  
    if index == -1:
        return [(index, -1)]
    else:
        swap_with = index + 1
        for j in range(index + 1, size):
            if (arr[j] > arr[index] and arr[j] < arr[swap_with]):
                swap_with = j
        return [(index, swap_with)]