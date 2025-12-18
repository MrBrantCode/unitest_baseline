"""
QUESTION:
Create a function `find_disparity(arr)` that calculates the difference between the maximum and minimum integers within a given array. The function should handle cases where the array contains duplicate integers, negative integers, or is empty. It should also return the positions of the maximum and minimum integers, returning the position of the first occurrence in case of multiple occurrences. The function should be able to handle arrays of up to 10^6 elements without exceeding time and space complexity limitations.
"""

def find_disparity(arr):
    # manage situations where the array may be empty
    if len(arr) == 0:
        return 'The provided array is empty'
    
    min_val = arr[0]
    max_val = arr[0]
    min_index = 0
    max_index = 0
    
    for i in range(1, len(arr)):
        # check if current element of array is lesser or greater than min or max
        if arr[i] < min_val:
            min_val = arr[i]
            min_index = i
        elif arr[i] > max_val:
            max_val = arr[i]
            max_index = i
    
    # calculate disparity between maximum and minimum integers
    disparity = max_val - min_val
    
    return disparity, min_index, max_index