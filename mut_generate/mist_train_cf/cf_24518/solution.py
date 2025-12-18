"""
QUESTION:
Design a function `max_index` that takes an array of integers as input and returns the index of the maximum element in the array. The function should assume that the input array is not empty and contains at least one element.
"""

def max_index(lst): 
    max_val = 0
    max_index = 0
    for i in range(len(lst)): 
        if lst[i] > max_val: 
            max_val = lst[i]
            max_index = i
    return max_index