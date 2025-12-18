"""
QUESTION:
Design a function named `maxSubArraySum` that calculates the maximum subarray sum in a given array. The function should take an array of integers as input and return an integer representing the maximum subarray sum. The array may contain both positive and negative integers, but it is guaranteed to contain at least one positive number. If the array contains only non-positive numbers, the function should return the maximum number in the array.
"""

def maxSubArraySum(array):
    """
    This function calculates the maximum subarray sum in a given array.
    
    Parameters:
    array (list): A list of integers containing at least one positive number.
    
    Returns:
    int: The maximum subarray sum.
    """
    maxSoFar = maxEndingHere = array[0]
    for i in range(1, len(array)):
        maxEndingHere = max(maxEndingHere + array[i], array[i])
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar