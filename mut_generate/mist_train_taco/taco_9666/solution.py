"""
QUESTION:
Given a collection of distinct integers, return all possible permutations.

Example:


Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

def generate_permutations(nums):
    def permute_nums(all_permutes, nums, cur_permute):
        if len(nums) == 0:
            all_permutes.append(cur_permute)
            return
        for i in range(len(nums)):
            num = nums[i]
            permute_nums(all_permutes, nums[0:i] + nums[i + 1:len(nums)], cur_permute + [num])
    
    all_permutes = []
    permute_nums(all_permutes, nums, [])
    return all_permutes