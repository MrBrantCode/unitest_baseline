"""
QUESTION:
Given an unsorted array of integers `nums`, return the length of the longest continuous increasing subsequence that can be achieved by changing at most one element in the array. The change should be such that the new value is strictly greater than the previous element and strictly less than the next element in the array. A continuous increasing subsequence is defined by two indices `l` and `r` (`l < r`) such that for each `l <= i < r`, `nums[i] < nums[i + 1]`. The function should be named `findLengthOfLCIS` and take `nums` as input. The input array `nums` satisfies `1 <= nums.length <= 10^5` and `-10^9 <= nums[i] <= 10^9`.
"""

def findLengthOfLCIS(nums):
    if not nums:
        return 0
    
    n = len(nums)
    prev, curr, prev_change = nums[0], 1, 0
    max_len = 1
    
    for i in range(1, n):
        if nums[i] > prev:
            curr += 1
            prev_change += 1
        elif nums[i] - 1 > nums[i-2] if i > 1 else nums[i] > nums[i-1]:
            curr = prev_change + 1
            prev_change = curr
        else:
            curr = prev_change = 1
        prev = nums[i]
        max_len = max(max_len, curr)
    
    return max_len