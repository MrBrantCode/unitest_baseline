"""
QUESTION:
Find the shortest subarray in a given array with a sum greater than or equal to a given number.

The function should be named `min_window`. It takes two parameters: `nums` (the given array) and `target` (the given number). The function should return the shortest subarray with a sum greater than or equal to the target. If no such subarray exists, the function's behavior is undefined.
"""

def min_window(nums, target):
    """
    Find the shortest subarray in a given array with a sum greater than or equal to a given number.

    Args:
        nums (list): The given array.
        target (int): The given number.

    Returns:
        list: The shortest subarray with a sum greater than or equal to the target.
    """
    left = 0
    curr_sum = 0
    min_len = float('inf')
    min_window = None

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = nums[left:right + 1]

            curr_sum -= nums[left]
            left += 1

    return min_window