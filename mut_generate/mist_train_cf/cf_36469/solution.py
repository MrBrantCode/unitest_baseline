"""
QUESTION:
Given an array of integers (1 <= length <= 10, -10 <= each integer <= 10) that may contain duplicates, write a function named `subsetsWithDup` that returns all unique possible subsets (power set) in any order, without including duplicate subsets in the result.
"""

def subsetsWithDup(nums):
    """
    Returns all unique possible subsets (power set) of the given array without including duplicate subsets.

    Args:
        nums (List[int]): An array of integers.

    Returns:
        List[List[int]]: A list of unique subsets.
    """
    def dfs(index, path):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            dfs(i+1, path+[nums[i]])

    nums.sort()
    res = []
    dfs(0, [])
    return res