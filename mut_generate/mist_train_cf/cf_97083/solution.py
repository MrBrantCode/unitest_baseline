"""
QUESTION:
Create a function `flatten_array(arr)` that takes a two-dimensional array `arr` as input and returns a one-dimensional array. The function should exclude any element from the input array that is a negative number and is divisible by 3. The function should include all other elements from the input array in the output array.
"""

def flatten_array(arr):
    return [element for sub_array in arr for element in sub_array if element >= 0 and element % 3 != 0]