"""
QUESTION:
Write a function `permuteUnique(nums)` that generates all distinct permutations of the input list `nums`, which may contain repeated elements. The function should return a list of lists, where each sublist is a unique permutation of the input list. The input list `nums` will contain between 1 and 8 elements, and each element will be an integer between -10 and 10.
"""

def permuteUnique(nums):
    def dfs(nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    nums.sort()
    res = []
    dfs(nums, [], res)
    return res