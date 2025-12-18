"""
QUESTION:
Create a function `permutations(nums)` that generates all possible permutations of a given list of unique integers `nums` using recursion and memoization. The function should return the permutations as a list of lists and handle sets of any length. Ensure that the function only generates permutations with unique values, avoiding duplicates in the permutations.
"""

def permuteUnique(nums):
    memo = {}

    def helper(nums):
        if len(nums) == 1:
            return [nums]

        if str(nums) in memo:
            return memo[str(nums)]

        result = []
        for i in range(len(nums)):
            if nums[i] in nums[:i]:
                continue
            rest = nums[:i] + nums[i+1:]
            permutations_rest = helper(rest)
            for p in permutations_rest:
                result.append([nums[i]] + p)

        memo[str(nums)] = result
        return result

    return helper(nums)