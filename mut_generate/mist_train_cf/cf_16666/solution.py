"""
QUESTION:
Create a function `find_duplicate_indices` that takes an array of at most 1000 positive integers as input and returns the indices of all duplicate values found. The function must have a time complexity of O(n) and a space complexity of O(1), excluding the space needed for the output.
"""

def find_duplicate_indices(arr):
    duplicate_indices = []
    for i in range(len(arr)):
        index = abs(arr[i]) - 1
        if arr[index] < 0:
            duplicate_indices.append(index)
        else:
            arr[index] = -arr[index]
    return duplicate_indices