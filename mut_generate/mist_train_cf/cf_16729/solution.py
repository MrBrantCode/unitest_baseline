"""
QUESTION:
Design a function named `find_max` that finds the maximum value and its corresponding index in a given array. The array can have a maximum length of 10^6, may contain duplicate elements and negative values, and the solution should have a time complexity of O(n), where n is the length of the array. The function should return a tuple containing the maximum value and its index.
"""

def find_max(array):
    max_value = array[0]
    max_index = 0
    
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
            max_index = i
    
    return (max_value, max_index)