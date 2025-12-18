"""
QUESTION:
Find the pair of elements in an array with the greatest difference where the larger element is located at an index greater than the smaller element. If multiple pairs have the same maximum difference, return the pair with the smallest index of the smaller element. If there are no pairs that satisfy the condition, return an empty array. The array can have duplicates. Implement this as a function called `find_max_difference`.
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