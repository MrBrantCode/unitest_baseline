"""
QUESTION:
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.



Note:
1 .
0 < nums[i] < 10000.
"""

def can_partition_k_subsets(nums, k):
    target, rem = divmod(sum(nums), k)
    if rem or max(nums) > target:
        return False
    
    n = len(nums)
    seen = [0] * n
    nums.sort(reverse=True)

    def dfs(k, index, current_sum):
        if k == 1:
            return True
        if current_sum == target:
            return dfs(k - 1, 0, 0)
        for i in range(index, n):
            if not seen[i] and current_sum + nums[i] <= target:
                seen[i] = 1
                if dfs(k, i + 1, current_sum + nums[i]):
                    return True
                seen[i] = 0
        return False
    
    return dfs(k, 0, 0)