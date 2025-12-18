"""
QUESTION:
Write a function, `find_combinations(nums: List[int], target: int) -> int`, that returns the number of distinct combinations of the given integers in `nums` that sum up to the `target`. You may assume that each input would have exactly one solution and that you may reuse the elements of `nums`. The order of the combinations does not matter.
"""

from typing import List

def combinationSum4(nums: List[int], target: int) -> int:
    memo = {}

    def find_combinations(target):
        if target < 0:
            return 0
        elif target == 0:
            return 1
        elif target in memo:
            return memo[target]

        count = 0
        for num in nums:
            count += find_combinations(target - num)
        memo[target] = count
        return count

    return find_combinations(target)