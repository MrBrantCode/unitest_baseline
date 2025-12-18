"""
QUESTION:
Given a list of integers, implement a function `maxLengthSubarray` that returns the maximum length of a contiguous subarray with a sum of zero. The function should take a list of integers as input and return an integer representing the maximum length. The input list can contain both positive and negative integers.
"""

def maxLengthSubarray(nums):
    """
    Returns the maximum length of a contiguous subarray with a sum of zero.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    int: The maximum length of a contiguous subarray with a sum of zero.
    """
    # Create a dictionary to store the running sum and its index.
    prefixSumIndex = {0: -1}
    maxLength = 0
    sumSoFar = 0

    for index, num in enumerate(nums):
        sumSoFar += num

        # If sumSoFar is seen before, then there is a zero-sum subarray. Check if it is maximum.
        if sumSoFar in prefixSumIndex:
            maxLength = max(maxLength, index - prefixSumIndex[sumSoFar])
        else:
            # If sumSoFar is not present in dictionary, then store it.
            prefixSumIndex[sumSoFar] = index 

    return maxLength