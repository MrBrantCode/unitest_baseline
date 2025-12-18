"""
QUESTION:
Implement a function `reverse_array` that takes an array as input and returns the array with its elements reversed. The function should have a time complexity of O(n), where n is the length of the input array, and use constant space complexity, modifying the array in place.
"""

def reverse_array(nums):
    """
    Reverses the input array in place with a time complexity of O(n) and constant space complexity.

    Args:
        nums (list): The input array to be reversed.

    Returns:
        list: The reversed array.
    """
    for i in range(len(nums)//2):
        nums[i], nums[-i-1] = nums[-i-1], nums[i]
    return nums