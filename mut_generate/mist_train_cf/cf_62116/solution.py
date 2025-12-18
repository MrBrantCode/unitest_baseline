"""
QUESTION:
You are given an integer array `nums`. The task is to determine the highest number of points that can be accumulated by executing a series of operations. In each operation, select any `nums[i]`, remove it, and gain `nums[i]` points, and then eliminate every element that is equal to `nums[i] - 1` or `nums[i] + 1`. 

Implement a function `deleteAndEarn(nums)` to solve this problem, where `1 <= nums.length <= 2 * 10^4` and `1 <= nums[i] <= 10^4`.
"""

def deleteAndEarn(nums):
    freq = [0]*10001

    for num in nums:
        freq[num] += num
    
    dp00, dp01 = 0, 0
    
    for i in range(10001):
        dp0 = max(dp00, dp01)	
        dp1 = dp00 + freq[i]		
        dp00, dp01 = dp0, dp1	
		
    return max(dp00, dp01)