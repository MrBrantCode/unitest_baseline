"""
QUESTION:
Given a numerical array `nums` and a positive integer `k`, determine if it's plausible to partition this array into `k` non-empty subsets, each boasting an equivalent sum. Implement a function `canPartitionKSubsets(nums, k)` that returns a boolean value indicating whether such a partition is possible. The function should adhere to the following constraints: `1 <= k <= len(nums) <= 16` and `0 < nums[i] < 10000`.
"""

def canPartitionKSubsets(nums, k):
    if k > len(nums):
        return False
    total_sum = sum(nums)
    if total_sum % k != 0:
        return False
    target = total_sum // k
    visit = [0] * len(nums)
    nums.sort(reverse=True)
    def dfs(k, curr_sum, curr_num, start):
        if k == 1:
            return True
        if curr_sum == target and curr_num > 0:
            return dfs(k-1, 0, 0, 0)
        for i in range(start, len(nums)):
            if visit[i] == 0 and curr_sum + nums[i] <= target:
                visit[i] = 1
                if dfs(k, curr_sum + nums[i], curr_num+1, i+1):
                    return True
                visit[i] = 0
        return False    
    return dfs(k, 0, 0, 0)