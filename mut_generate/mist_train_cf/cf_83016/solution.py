"""
QUESTION:
Create a function called `optimize` that takes an array of non-duplicate integers as input and returns a list of tuples. Each tuple contains the smallest index of an element that isn't larger than its subsequent element, and the index of the next smaller element with which it can be replaced to enhance the sequence. If no such element exists, return [(index: -1, replace_with: -1)].
"""

def optimize(arr):
    replace = []
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            for j in range(i+1, len(arr)):
                if arr[j] < arr[i]:
                    replace.append((i, j))
                    break
    if replace: 
        return replace
    else: 
        return [(-1, -1)]