"""
QUESTION:
Given a list of integers `nums` and a positive integer `k`, determine if it's possible to partition `nums` into `k` non-empty subsets, each having an identical sum. The function `canPartitionKSubsets(nums, k)` should return a boolean indicating whether such partitioning is feasible. Constraints: `1 <= k <= len(nums) <= 16` and `0 < nums[i] < 10000`.
"""

def canPartitionKSubsets(nums, k):
    target, rem = divmod(sum(nums), k)
    if rem != 0:
        return False

    def search(groups):
        if not nums:
            return True
        v = nums.pop()
        for i, group in enumerate(groups):
            if group + v <= target:
                groups[i] += v
                if search(groups):
                    return True
                groups[i] -= v
            if not group:
                break
        nums.append(v)
        return False

    nums.sort()
    if nums[-1] > target:
        return False
    return search([0]*k)