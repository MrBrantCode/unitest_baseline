"""
QUESTION:
Write a function `find_swap_values(arr1, arr2)` that takes two integer arrays `arr1` and `arr2` as input. The function should return a pair of values, one from `arr1` and one from `arr2`, such that swapping them would make the sum of the two arrays equal. If no such pair exists, the function should return `None`. The function should assume that the input arrays are not empty and that the elements are integers.
"""

def find_swap_values(arr1, arr2):
    # calculate sum of both lists and their difference
    sum1, sum2 = sum(arr1), sum(arr2)
    difference = sum1 - sum2
    
    # the difference must be even to swap 2 values
    if difference % 2 != 0:
        return None
    difference //= 2
    
    # get all pairs where the difference is equal to the desired difference
    values = [(i, j) for i in arr1 for j in arr2 if i - j == difference]
    return values[0] if values else None