"""
QUESTION:
Write a function `threeSumClosest(nums, target)` that takes a list `nums` of n integers and an integer `target` as input. The function should return the sum of three integers in `nums` that is closest to `target`. The length of `nums` should be no less than 3 and no more than 10^3, and each integer in `nums` should be no less than -10^3 and no more than 10^3. The `target` should be no less than -10^4 and no more than 10^4. It is assumed that each input set will yield exactly one unique solution.
"""

def threeSumClosest(nums, target):
    nums.sort()
    diff = float('inf')
    for i in range(len(nums)):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if abs(target - sum) < abs(diff):
                diff = target - sum
            if sum < target:
                lo += 1
            else:
                hi -= 1
        if diff == 0:
            break
    return target - diff