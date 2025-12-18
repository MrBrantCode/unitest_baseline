"""
QUESTION:
Write a function named `normalize_array` that takes an array of non-negative numbers as input and returns a new array where the sum of its elements equals 1. The function should divide each element in the input array by the sum of all elements in the array. If the sum of the input array is zero, the function should return an array of zeros with the same length as the input array.
"""

def normalize_array(nums):
    """
    Normalize an array of non-negative numbers to have a sum of 1.

    Args:
        nums (list): A list of non-negative numbers.

    Returns:
        list: A new list where the sum of its elements equals 1.
    """
    total = sum(nums)
    if total == 0:
        return [0] * len(nums)
    return [num / total for num in nums]