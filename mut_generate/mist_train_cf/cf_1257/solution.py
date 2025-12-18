"""
QUESTION:
Write a function `two_sum` that takes two inputs: an array of integers and a target sum. The function should return `True` if any two distinct integers in the array add up to the target sum, and `False` otherwise. The function should have a time complexity of O(n) and a space complexity of O(n), and it should not use any additional data structures such as sets or dictionaries.
"""

def two_sum(nums, target):
    """
    This function checks if any two distinct integers in the given array add up to the target sum.

    Args:
        nums (list): A list of integers.
        target (int): The target sum.

    Returns:
        bool: True if any two distinct integers add up to the target sum, False otherwise.
    """
    nums.sort()  # Sort the array in non-decreasing order
    left = 0  # Initialize the left pointer
    right = len(nums) - 1  # Initialize the right pointer

    while left < right:  # Continue until the two pointers meet
        current_sum = nums[left] + nums[right]  # Calculate the sum of the elements at the two pointers
        if current_sum == target:  # If the sum is equal to the target
            return True
        elif current_sum < target:  # If the sum is less than the target
            left += 1  # Move the left pointer to the right
        else:  # If the sum is greater than the target
            right -= 1  # Move the right pointer to the left

    return False  # If no two distinct integers add up to the target sum, return False