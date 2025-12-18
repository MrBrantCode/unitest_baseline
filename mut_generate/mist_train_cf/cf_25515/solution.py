"""
QUESTION:
Create a function called `find_longest_subarray` that takes two parameters: an array of integers and a target sum. The function should return the longest subarray within the given array where the sum of its elements is less than the target sum.
"""

def find_longest_subarray(arr, target_sum):
    """
    Returns the longest subarray within the given array where the sum of its elements is less than the target sum.

    Parameters:
    arr (list): An array of integers.
    target_sum (int): The target sum.

    Returns:
    list: The longest subarray where the sum of its elements is less than the target sum.
    """
    longest_subarray = []
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum < target_sum and len(arr[i: j + 1]) > len(longest_subarray):
                longest_subarray = arr[i: j + 1]
    return longest_subarray