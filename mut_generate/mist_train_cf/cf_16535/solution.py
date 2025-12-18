"""
QUESTION:
Find the pair of elements in an array that have the greatest difference, with the larger element located at an index greater than the smaller element. If multiple pairs have the same maximum difference, return the pair with the smallest index of the smaller element. If there are no pairs that satisfy the condition, return an empty array.

The input array can contain duplicates and the solution must handle them correctly. Implement the function `find_max_difference(arr)`, where `arr` is the input array of integers.
"""

def find_max_difference(arr):
    max_diff = 0
    result = []
    min_val = float('inf')
    
    for num in arr:
        if num < min_val:
            min_val = num
        diff = num - min_val
        if diff > max_diff:
            max_diff = diff
            result = [min_val, num]
    
    return result