"""
QUESTION:
Write a function `three_sum` that takes a list of unique integers and a target number as input, and returns a list of three indices of the numbers in the list whose sum is equal to the target number. If there are multiple triplets, return any one of them. If no such triplets exist, return an empty list.
"""

def three_sum(nums, target):
    nums = sorted((e, i) for i, e in enumerate(nums))
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i][0] + nums[l][0] + nums[r][0]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return sorted([nums[i][1], nums[l][1], nums[r][1]])
    return []