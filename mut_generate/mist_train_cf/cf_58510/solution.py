"""
QUESTION:
Given an array of integers `nums` and an integer `k`, write a function `numberOfSubarrays(nums, k)` that returns the number of continuous subarrays with exactly `k` odd numbers and the sum of the elements in the subarray divisible by `k`.

The length of `nums` is between 1 and 50,000, and each element in `nums` is between 1 and 10^5. The value of `k` is between 1 and the length of `nums`.
"""

def numberOfSubarrays(nums, k):
    remainderCount = {0: 1} 
    prefixSum = cnt = oddCnt = 0

    for i in range(len(nums)):
        oddCnt += nums[i] % 2  # Update odd count
        if oddCnt >= k: 
            cnt += remainderCount.get(oddCnt - k, 0)
        remainderCount[oddCnt] = remainderCount.get(oddCnt, 0) + 1
    return cnt