"""
QUESTION:
Find the maximum length of the longest consecutive increasing subsequence in an array. The function should take an array of integers as input and return the length of the longest consecutive increasing subsequence. The subsequence is considered increasing if each element is strictly greater than the previous one.
"""

def findLengthOfLCIS(nums):
    ans = 1
    j = 0

    for i in range(len(nums) - 1): 
        if (nums[i+1] - nums[i] > 0): 
            j += 1
            ans = max(ans, j+1)
        else:  
            j = 0
    return ans