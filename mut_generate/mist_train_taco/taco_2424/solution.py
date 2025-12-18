"""
QUESTION:
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2



Note:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

def count_subarrays_with_sum(nums: list[int], k: int) -> int:
    dic = {}
    numSum = 0
    dic[0] = 1
    ans = 0
    for num in nums:
        numSum += num
        if numSum - k in dic:
            ans += dic[numSum - k]
        if numSum in dic:
            dic[numSum] += 1
        else:
            dic[numSum] = 1
    return ans