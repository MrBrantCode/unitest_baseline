"""
QUESTION:
Write a function named `move_zeros_to_end` that takes an array of integers as input and returns the modified array with all zeros moved to the end, while maintaining the order of the non-zero elements. The function should be able to handle large input arrays (up to 10^5 elements) with both positive and negative integers, and duplicates.
"""

def move_zeros_to_end(nums):
    """
    Move all zeros to the end of the given array while maintaining the order of non-zero elements.

    Args:
        nums (list): The input array of integers.

    Returns:
        list: The modified array with all zeros moved to the end.
    """
    # Initialize the index where the next non-zero element should be placed
    zero_index = 0

    # Iterate through the input array
    for i in range(len(nums)):
        # If the current element is non-zero, swap it with the element at the current index
        if nums[i] != 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            # Increment the current index by 1
            zero_index += 1

    # Return the modified array
    return nums