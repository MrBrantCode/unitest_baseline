"""
QUESTION:
Write a function `numberOfSubarrays(nums, k)` that takes an array of integers `nums` and an integer `k` as input and returns the number of nice sub-arrays. A continuous subarray is called nice if there are `k` odd numbers on it, the sum of the elements in the subarray is divisible by `k`, the length of the subarray is less than or equal to `2k`, and the sum of the squares of the elements in the subarray is divisible by `k`. The length of `nums` is between 1 and 50000, and each element in `nums` and `k` is between 1 and 10^5.
"""

from collections import deque

def numberOfSubarrays(nums, k):
    n = len(nums)
    odd_indices = deque()
    count = 0
    for i in range(n):
        if nums[i] % 2 == 1:
            odd_indices.append(i)
        if len(odd_indices) == k:
            start = i
            left_count = 1
            if len(odd_indices) > 1:
                previous_odd = odd_indices.popleft()
                left_count = previous_odd - odd_indices[0] + 1
            while start < n and nums[start] % 2 == 0:
                start += 1
            right_count = start - i
            subarray = nums[odd_indices[0]:start + 1]
            sum_subarray = sum(subarray)
            sum_squares_subarray = sum([num * num for num in subarray])
            if sum_subarray % k == 0 and len(subarray) <= 2 * k and sum_squares_subarray % k == 0:
                count += left_count * right_count
    return count