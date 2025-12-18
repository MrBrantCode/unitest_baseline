"""
QUESTION:
Create a function `find_duplicate_indices(arr)` that takes an array of positive integers as input and returns the indices of all duplicate values in the array. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array, which will not exceed 1000.
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