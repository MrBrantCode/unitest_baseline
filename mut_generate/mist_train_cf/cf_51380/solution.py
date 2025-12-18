"""
QUESTION:
Given an array of integers `nums` and an integer `limit`, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to `limit` and the sum of the elements in this subarray is maximum. If there are multiple subarrays with the same length and sum, return any one of them.

The function should be named `longestSubarray` and take two parameters: `nums` and `limit`. 

Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^9`, and `0 <= limit <= 10^9`.
"""

from collections import deque

def longestSubarray(nums, limit):
    min_deque, max_deque = deque(), deque()
    left = 0
    ans = 0
    max_length = 0
    max_sum = 0
    current_sum = 0

    for right, num in enumerate(nums):
        while max_deque and num > max_deque[-1]: 
            max_deque.pop()

        while min_deque and num < min_deque[-1]: 
            min_deque.pop()

        max_deque.append(num)
        min_deque.append(num)
        current_sum += num

        if max_deque[0] - min_deque[0] > limit:
            if max_deque[0] == nums[left]:
                max_deque.popleft()
            if min_deque[0] == nums[left]:
                min_deque.popleft()
            current_sum -= nums[left]
            left += 1

        if right - left + 1 > max_length or (right - left + 1 == max_length and current_sum > max_sum):
            max_length = right - left + 1
            max_sum = current_sum

    return max_length