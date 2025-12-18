"""
QUESTION:
Create a function named `find_duplicates` that takes an array of integers as input and returns a list of indices of all duplicate values found in the array. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def find_duplicates(arr):
    duplicate_indices = []
    for i in range(len(arr)):
        index = abs(arr[i]) - 1
        if arr[index] < 0:
            duplicate_indices.append(index)
        else:
            arr[index] = -arr[index]
    return duplicate_indices