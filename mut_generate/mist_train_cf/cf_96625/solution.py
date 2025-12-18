"""
QUESTION:
Write a function `find_sum_of_three` that takes an array of integers and a target sum `n` as input. The function should return the indices of three numbers in the array whose sum equals `n`. The function must have a time complexity of O(n^2) and should not use any additional data structures or sorting algorithms.
"""

def find_sum_of_three(nums, target):
    """
    Returns the indices of three numbers in the array whose sum equals the target sum.

    Args:
        nums (list): A list of integers.
        target (int): The target sum.

    Returns:
        list: A list of indices of three numbers in the array whose sum equals the target sum, or None if no such combination exists.
    """
    nums_len = len(nums)
    for i in range(nums_len - 2):
        left, right = i + 1, nums_len - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return [i, left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return None