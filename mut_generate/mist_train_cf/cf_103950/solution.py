"""
QUESTION:
Create a function named `linear_search` that takes two parameters: an array of integers and a target integer. The function should return a list of indices of all occurrences of the target element in the array. If the target element is not found, return an empty list.
"""

def linear_search(array, target):
    indices = []
    for i in range(len(array)):
        if array[i] == target:
            indices.append(i)
    return indices