"""
QUESTION:
Given a list of integers, create a function `create_arrays(arr)` that generates two lists. The first list should contain each element of the input list raised to the power of three. The second list should contain the cumulative sum of the cubes of all previous numbers including the current one in the input list. The function should be optimized to handle input lists of up to 10⁶ elements.
"""

from itertools import accumulate

def create_arrays(arr):
    cubes = [i**3 for i in arr]
    sums = list(accumulate(cubes))
    return cubes, sums