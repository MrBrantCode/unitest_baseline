"""
QUESTION:
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:


Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

def generate_unique_permutations(nums):
    if not nums:
        return []
    
    nums.sort()
    n = len(nums)
    res = [nums[:]]
    i = n - 1
    
    while i > 0:
        if nums[i - 1] < nums[i]:
            j = n - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            (nums[i - 1], nums[j]) = (nums[j], nums[i - 1])
            nums[i:] = sorted(nums[i:])
            res.append(nums[:])
            i = n - 1
        else:
            i -= 1
    
    return res