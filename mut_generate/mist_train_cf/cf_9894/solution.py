"""
QUESTION:
Write a function `find_combinations(nums, target)` that returns the number of distinct combinations of the given integers in `nums` that sum up to the `target`. You may assume that each input would have exactly one solution and that you may reuse the elements of `nums`. The order of the combinations does not matter.
"""

from typing import List

def find_combinations(nums: List[int], target: int) -> int:
    """
    Returns the number of distinct combinations of the given integers in `nums` that sum up to the `target`.
    
    :param nums: A list of integers.
    :type nums: List[int]
    :param target: The target sum.
    :type target: int
    :return: The number of distinct combinations.
    :rtype: int
    """

    count = 0

    def backtrack(remain, comb, start):
        nonlocal count
        if remain == 0:
            count += 1
            return
        elif remain < 0:
            return
        for i in range(start, len(nums)):
            comb.append(nums[i])
            backtrack(remain - nums[i], comb, i)
            comb.pop()

    backtrack(target, [], 0)
    return count