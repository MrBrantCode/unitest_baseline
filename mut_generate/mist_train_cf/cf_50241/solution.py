"""
QUESTION:
Write a function `maximumScore(nums, k, m)` that takes an array of integers `nums`, an integer `k`, and an integer `m` as input, and returns the maximum possible score of a good subarray where the score is defined as the minimum value in the subarray multiplied by its length, the subarray must include index `k`, and its length must be less than or equal to `m`. The constraints are: `1 <= nums.length <= 105`, `1 <= nums[i] <= 2 * 104`, `0 <= k < nums.length`, and `1 <= m <= nums.length`.
"""

def maximumScore(nums, k, m):
    n = len(nums)
    left, right = k, k
    ans = score = nums[k]
    minVal = nums[k]
    
    while right - left + 1 < m:
        if left == 0:
            right += 1
        elif right == n - 1:
            left -= 1
        elif nums[left - 1] < nums[right + 1]:
            right += 1
        else:
            left -= 1
            
        minVal = min(minVal, nums[left], nums[right])
        ans = max(ans, minVal * (right - left + 1))
        
    return ans