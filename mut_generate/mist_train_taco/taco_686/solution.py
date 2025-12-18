"""
QUESTION:
Given a set of n non-negative integers, and a value m, determine if there is a subset of the given set with sum divisible by m.
Example 1:
Input: 
n = 4 m = 6 
nums[] = {3 1 7 5}
Output:
1
Explanation:
If we take the subset {7, 5} then sum
will be 12 which is divisible by 6.
Example 2:
Input:
n = 3, m = 5
nums[] = {1 2 6}
Output:
0
Explanation: 
All possible subsets of the given set are 
{1}, {2}, {6}, {1, 2}, {2, 6}, {1, 6}
and {1, 2, 6}. There is no subset whose
sum is divisible by 5.
Your Task:
You don't need to read or print anything. Your task is to complete the function DivisibleByM() which takes the given set and m as input parameter and returns 1 if any of the subset(non-empty) sum is divisible by m otherwise returns 0.
Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n)
Constraints:
1 <= elements in set <= 1000
1 <= n, m <= 1000
"""

def has_subset_sum_divisible_by_m(nums, m):
    def f(i, rem, nums, dp):
        if rem == 0:
            return True
        if i >= len(nums):
            return False
        if dp[i][rem] != -1:
            return dp[i][rem]
        if rem == -1:
            take = f(i + 1, nums[i] % m, nums, dp)
            ntake = f(i + 1, rem, nums, dp)
        else:
            take = f(i + 1, (rem + nums[i]) % m, nums, dp)
            ntake = f(i + 1, rem, nums, dp)
        dp[i][rem] = take or ntake
        return take or ntake
    
    dp = [[-1] * (m + 1) for _ in range(len(nums))]
    return int(f(0, -1, nums, dp))