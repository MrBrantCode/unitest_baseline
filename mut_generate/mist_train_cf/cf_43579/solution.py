"""
QUESTION:
Write a function called `find_missing(arr)` that takes a 2D array of integers as input and returns the smallest positive integer missing from the array. The function should be able to handle arrays of any size, including duplicates and negative numbers.
"""

def find_missing(arr):
    flat_list = [item for sublist in arr for item in sublist]
    sorted_list = sorted(set([i for i in flat_list if i > 0]))
    p = next((i for i, num in enumerate(sorted_list, start=1) if i != num), None)
    
    if p is None:
        if len(sorted_list) == 0:
            return 1
        else:
            return sorted_list[-1] + 1
    else:
        return p