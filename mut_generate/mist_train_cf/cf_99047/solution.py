"""
QUESTION:
Write a function named `max_sum_neg_odd` that calculates the highest sum of consecutively appearing negative numbers that appear in odd-indexed positions of an array. The function should use recursion instead of a loop and consider the highest sum found so far. The function should take an array as input and return the highest sum of consecutively appearing negative numbers that appear in odd-indexed positions of the array.
"""

def max_sum_neg_odd(arr, i=1, curr_sum=0, max_sum=-float('inf')):
    """
    Calculates the highest sum of consecutively appearing negative numbers that appear in odd-indexed positions of an array.

    Args:
    arr (list): The input array.
    i (int): The current index being evaluated. Defaults to 1.
    curr_sum (int): The current sum of negative numbers. Defaults to 0.
    max_sum (int): The maximum sum found so far. Defaults to -infinity.

    Returns:
    int: The highest sum of consecutively appearing negative numbers that appear in odd-indexed positions of the array.
    """
    if i >= len(arr):
        # base case
        return max_sum
    if arr[i] < 0 and i % 2 != 0:
        # if the current number is negative and in an odd-indexed position, add it to the current sum
        curr_sum += arr[i]
        if curr_sum > max_sum:
            # if the current sum is greater than the max sum, update the max sum
            max_sum = curr_sum
    else:
        # if the current number is not negative or is in an even-indexed position, reset the current sum
        curr_sum = 0
    # recursively call the function for the next index
    return max_sum_neg_odd(arr, i+1, curr_sum, max_sum)