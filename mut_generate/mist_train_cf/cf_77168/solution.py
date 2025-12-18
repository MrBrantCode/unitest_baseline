"""
QUESTION:
Write a function `canIWin` that takes two integers `maxChoosableInteger` and `desiredTotal` as input and returns `True` if the first player can force a win in a modified "100 game" where players take turns choosing integers from 1 to `maxChoosableInteger` without replacement and alternating between odd and even numbers, and `False` otherwise. Assume both players play optimally and follow the odd-even rule. The constraints are `1 <= maxChoosableInteger <= 20` and `0 <= desiredTotal <= 300`.
"""

def canIWin(maxChoosableInteger, desiredTotal):
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal: 
        return False
    memo = {}
    def helper(nums, target):
        hash = str(nums)
        if hash in memo:
            return memo[hash]

        if nums and nums[-1] >= target:
            return True

        for i in range(len(nums) - 1, -1, -1):
            if not helper(nums[:i] + nums[i + 1:], target - nums[i]):
                memo[hash] = True
                return True

        memo[hash] = False
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)