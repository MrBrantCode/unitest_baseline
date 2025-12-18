"""
QUESTION:
Find all pairs of identical numbers in a given list of integers that are equidistant from the middle of the list. The function should take a list of integers as input and return a list of tuples, where each tuple represents a symmetric pair of numbers.
"""

def symmetric_pairs(nums):
    """
    Function to find symmetric pairs in a list of integers.

    Arguments:
    nums {list} -- List of integers to search for symmetric pairs.

    Returns:
    List of tuples representing symmetric pairs.
    """
    pairs = []
    mid = len(nums) // 2
    for i in range(mid):
        if nums[i] == nums[len(nums) - i - 1]:
            pairs.append((nums[i], nums[len(nums) - i - 1]))
    return pairs