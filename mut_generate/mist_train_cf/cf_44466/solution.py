"""
QUESTION:
Write a function `findMissingRanges(nums, lower, upper)` that takes a sorted, unique integer array `nums` and an inclusive range `[lower, upper]` as input, and returns the smallest sorted list of ranges that encapsulate every missing number precisely. 

Each range in the list should be represented as `"a->b"` if `a != b` or `"a"` if `a == b`. The given constraints are `-10^9 <= lower <= upper <= 10^9`, `0 <= nums.length <= 100`, and `lower <= nums[i] <= upper`.
"""

def findMissingRanges(nums, lower, upper):
    res = []
    nums = [lower - 1] + nums + [upper + 1]

    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            if nums[i - 1] + 1 == nums[i] - 1:
                res.append(str(nums[i - 1] + 1))
            else:
                res.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))
    
    return res