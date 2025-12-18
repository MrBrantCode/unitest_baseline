"""
QUESTION:
Create a function named `upward_trajectory` that takes a multidimensional array `arr` as input. The function should return a list of dimension indices where all elements in that dimension are in strictly ascending order. The input array can contain integers and floating point numbers.
"""

def upward_trajectory(arr):
    dimensions = range(len(arr))
    dimensions_upward = []
    for dimension in dimensions:
        if all(i < j for i, j in zip(arr[dimension], arr[dimension][1:])):
            dimensions_upward.append(dimension)
    return dimensions_upward