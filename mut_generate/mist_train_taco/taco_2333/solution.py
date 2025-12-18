"""
QUESTION:
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:


Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

def generate_subsets_without_duplicates(nums):
    def dfs(idx, path):
        subsets.append(path)
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            dfs(i + 1, path + [nums[i]])
    
    nums.sort()
    subsets = []
    dfs(0, [])
    return subsets