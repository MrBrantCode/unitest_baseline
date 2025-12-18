"""
QUESTION:
Given an array of integers, write a function `three_sum` that identifies all unique triplets of numbers in the array whose combined sum equates to 0. The function should ignore duplicate triplets and return the result as a list of tuples. The input array can contain duplicate numbers. The function should be efficient for relatively small lists of numbers.
"""

def three_sum(nums):
    """
    Identifies all unique triplets of numbers in the array whose combined sum equates to 0.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of tuples, where each tuple is a unique triplet that sums to zero.
    """
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1; r -= 1
    return res