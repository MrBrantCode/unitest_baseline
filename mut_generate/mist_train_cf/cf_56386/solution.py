"""
QUESTION:
Find the missing values in a monotonically ascending sequence of integers from 1 to the maximum value in the sequence.

The function should take an array of integers as input and return a list of missing integers in the sequence. The sequence starts from 1 and has a step of 1. The input array may not contain all integers in the sequence from 1 to its maximum value, and the function should identify the missing integers.
"""

def find_missing_values(arr):
    """
    Find missing values in a monotonically ascending sequence of integers.

    Args:
    arr (list): A list of integers representing the sequence.

    Returns:
    list: A list of missing integers in the sequence.
    """
    max_val = max(arr)
    full_seq = list(range(1, max_val + 1))
    missing_values = [i for i in full_seq if i not in arr]
    return missing_values