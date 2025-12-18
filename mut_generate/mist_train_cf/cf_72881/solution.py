"""
QUESTION:
Create a function named 'indices_of_item' that takes an array 'arr' and an 'item' as input, and returns a list of indices where 'item' occurs in 'arr'. Do not use built-in methods to find the indices.
"""

def indices_of_item(arr, item):
    indices = [] 
    for i in range(len(arr)):
        if arr[i] == item:
            indices.append(i)
    return indices