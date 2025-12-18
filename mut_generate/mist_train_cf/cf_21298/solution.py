"""
QUESTION:
Write a function `sort_array(arr)` that takes an array of pairs of integers as input and returns the sorted array. The array should be sorted in ascending order based on the second element of each pair. If two pairs have the same second element, they should be sorted in descending order based on the first element. The input array size will be at most 10^6 and the values of the elements will be between -10^9 and 10^9.
"""

def sort_array(arr):
    arr.sort(key=lambda x: (x[1], -x[0]))
    return arr