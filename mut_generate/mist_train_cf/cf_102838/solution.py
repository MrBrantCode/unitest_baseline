"""
QUESTION:
Write a function `find_maximum_element` that finds the maximum element in a given 2-dimensional array, which can contain both positive and negative numbers. The function should return the maximum element found in the array. The input array will be a list of lists of integers.
"""

def find_maximum_element(arr):
    max_element = float('-inf')  # Initialize the maximum element as negative infinity
    
    for row in arr:
        for element in row:
            if element > max_element:
                max_element = element
    
    return max_element