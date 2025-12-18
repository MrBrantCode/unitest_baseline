"""
QUESTION:
Find a function called `find_pair` that takes two arrays of integers as input. The function should return a pair of values, one from each array, that can be swapped to make the sums of the two arrays equal. If no such pair exists, return -1.
"""

def find_pair(arr1, arr2):
    """
    This function takes two arrays of integers as input and returns a pair of values, 
    one from each array, that can be swapped to make the sums of the two arrays equal. 
    If no such pair exists, return -1.
    
    Args:
    arr1 (list): The first array of integers.
    arr2 (list): The second array of integers.
    
    Returns:
    tuple: A pair of values, one from each array, that can be swapped to make the sums of the two arrays equal. 
           If no such pair exists, return -1.
    """
    
    sum_arr1 = sum(arr1)
    sum_arr2 = sum(arr2)
    diff = abs(sum_arr1 - sum_arr2)

    for x in arr1:
        for y in arr2:
            if abs((sum_arr1 - x + y) - (sum_arr2 - y + x)) == 0:
                return (x, y)

    return -1