"""
QUESTION:
Write a function `generate_permutations(nums)` that takes a list of distinct integers `nums` as input and returns a list of all possible permutations of `nums` in lexicographic order without using any built-in functions or libraries for generating permutations.
"""

def generate_permutations(nums):
    if not nums:
        return []

    permutations = []

    def backtrack(start, end):
        if start == end:
            permutations.append(nums[:])

        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1, end)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0, len(nums))
    permutations.sort()
    return permutations