"""
QUESTION:
Create a function named `create_zero_array` that takes an integer `n` as input and returns an array of size `n` with all values initialized to 0. The function should have a time complexity of O(n) and a space complexity of O(1), but note that the space complexity requirement may not be achievable due to the need to allocate memory for the array.
"""

def create_zero_array(n):
    return [0] * n