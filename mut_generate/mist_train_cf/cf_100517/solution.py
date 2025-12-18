"""
QUESTION:
Create a function named `permutations` that generates all possible permutations of a given list of integers and returns them as a list of lists. The function should use recursion and memoization to handle lists of any length efficiently. The function should also ensure that the input list contains unique values and generates permutations without duplicates.
"""

def permutations(nums):
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