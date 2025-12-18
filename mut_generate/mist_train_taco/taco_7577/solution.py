"""
QUESTION:
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.


Example 1:


Input: nums = [1,2,3,1], k = 3, t = 0
Output: true



Example 2:


Input: nums = [1,0,1,1], k = 1, t = 2
Output: true



Example 3:


Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""

def contains_nearby_almost_duplicate(nums, k, t):
    if len(nums) < 2 or k <= 0 or t < 0:
        return False
    if t == 0:
        visited = set()
        for (i, n) in enumerate(nums):
            if n in visited:
                return True
            visited.add(n)
            if i >= k:
                visited.remove(nums[i - k])
        return False
    bucket = {}
    for (i, n) in enumerate(nums):
        b = n // t
        if b in bucket:
            return True
        if b + 1 in bucket and abs(bucket[b + 1] - n) <= t:
            return True
        if b - 1 in bucket and abs(bucket[b - 1] - n) <= t:
            return True
        bucket[b] = n
        if i >= k:
            del bucket[nums[i - k] // t]
    return False