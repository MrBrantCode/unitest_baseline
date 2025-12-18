"""
QUESTION:
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:


       All numbers (including target) will be positive integers.
       The solution set must not contain duplicate combinations.


Example 1:


Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]


Example 2:


Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

def find_unique_combinations(candidates, target):
    def dfs(i, val, path):
        while i < len(candidates):
            num = candidates[i]
            val_ = val + num
            path_ = path + [num]
            if val_ > target:
                return
            elif val_ == target:
                ans.append(path_)
                return
            dfs(i + 1, val_, path_)
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            i += 1
    
    candidates = sorted(candidates)
    ans = []
    dfs(0, 0, [])
    return ans