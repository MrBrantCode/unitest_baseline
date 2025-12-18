"""
QUESTION:
Write a function `tripleAndSum` that takes in an array of positive integers and returns an object with two values: the input array with each element tripled and the sum of the original array. The function should use constant extra space, without creating any additional arrays or objects, and have a time complexity of O(n), where n is the length of the input array.
"""

def tripleAndSum(nums):
    """
    This function takes an array of positive integers, triples each element in-place, 
    and returns a tuple containing the modified array and the sum of the original array.

    Args:
        nums (list): A list of positive integers.

    Returns:
        tuple: A tuple containing the modified array with each element tripled and 
        the sum of the original array.
    """
    total_sum = 0
    for i, num in enumerate(nums):
        total_sum += num
        nums[i] *= 3
    return nums, total_sum