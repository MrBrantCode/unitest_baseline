"""
QUESTION:
Write a function `permute(nums)` that generates all unique permutations of a given list of integers without using any built-in method or external libraries. The function should handle duplicate values in the list and be optimized for space complexity. The input list `nums` contains integers and may contain duplicate values. The output should be a list of lists, where each sublist is a unique permutation of the input list.
"""

def permute(nums):
    def backtrack(start, end):
        # if we are at the end, we have a complete permutation
        if start == end:
            result.add(tuple(nums))
        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]  # swap
            # use next integers to complete the permutations
            backtrack(start + 1, end)
            nums[start], nums[i] = nums[i], nums[start]  # backtrack

    result = set()
    backtrack(0, len(nums))
    return list(list(i) for i in result)  # convert back into lists