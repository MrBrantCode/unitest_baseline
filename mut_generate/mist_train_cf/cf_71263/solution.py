"""
QUESTION:
Implement the `linear_search` function to find an index of a given element `x` in an unsorted list `arr`. If `x` is not found in the list, return -1. Analyze the time and space complexity of the algorithm in terms of Big O notation, considering best, average, and worst-case scenarios, and discuss potential trade-offs between time and space complexities.
"""

def linear_search(arr, x):
    for i in range(len(arr)): 
        if arr[i] == x:
            return i 
    return -1