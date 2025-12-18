"""
QUESTION:
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:


Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

def find_closest_sum(nums, target):
    size = len(nums)
    if size < 3:
        return 0
    nums.sort()
    i = 0
    ans = nums[0] + nums[1] + nums[size - 1]
    while i < size - 2:
        tmp = target - nums[i]
        j = i + 1
        k = size - 1
        while j < k:
            if nums[j] + nums[k] == tmp:
                return target
            if nums[j] + nums[k] > tmp:
                if nums[j] + nums[j + 1] >= tmp:
                    if nums[j] + nums[j + 1] - tmp < abs(ans - target):
                        ans = nums[i] + nums[j] + nums[j + 1]
                    break
                tmpans = nums[i] + nums[j] + nums[k]
                if tmpans - target < abs(ans - target):
                    ans = tmpans
                k -= 1
            else:
                if nums[k] + nums[k - 1] <= tmp:
                    if tmp - nums[k] - nums[k - 1] < abs(ans - target):
                        ans = nums[i] + nums[k - 1] + nums[k]
                    break
                tmpans = nums[i] + nums[j] + nums[k]
                if target - tmpans < abs(ans - target):
                    ans = tmpans
                j += 1
        i += 1
        if ans == target:
            return target
    return ans