"""
QUESTION:
Create a function `check_pairs_optimized` that takes a 2D array and a difference value `diff` as input. The function should return all pairs of elements in the array where the difference between the elements is less than or equal to `diff`. The function should not use any built-in functions to find pairs, and it should be optimized for large arrays. The input array can be of any size (n x n, where n is a positive integer).
"""

def check_pairs_optimized(array, diff):
    # flatten and sort the array
    sorted_array = sorted([item for sublist in array for item in sublist])
    
    # initialize pairs list
    pairs = []
  
    # traverse the sorted array
    for i in range(len(sorted_array) - 1):
        # check if adjacent elements have a difference less than or equal to the given diff
        if abs(sorted_array[i] - sorted_array[i+1]) <= diff:
            pairs.append((sorted_array[i], sorted_array[i+1]))
    return pairs