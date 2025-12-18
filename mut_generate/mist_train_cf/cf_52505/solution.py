"""
QUESTION:
Write a function `validSubarrays(nums)` that takes an array `nums` of integers as input, where `1 <= len(nums) <= 50000` and `0 <= nums[i] <= 100000` for all `i`. The function should return the number of non-empty continuous subarrays that satisfy two conditions: 
- The leftmost element of the subarray is not larger than other elements in the subarray.
- The sum of the elements in the subarray is an even number.
"""

def validSubarrays(nums):
    stack, res, prefix = [], 0, {0: [0]}
    for x in nums:
        while stack and x < stack[-1][0]:
            val, idx = stack.pop()
            if idx in prefix:
                evens = prefix[idx]
                if evens:
                    res += sum(j < idx for j in evens)
                del prefix[idx]
        cur = len(prefix) and max(prefix.keys()) + 1 or 0
        if not cur & 1 in prefix:
            prefix[cur & 1] = []
        for p in list(prefix.keys()):
            prefix[p].append(cur)
        stack.append((x, cur))
    while stack:
        val, idx = stack.pop()
        if idx in prefix:
            evens = prefix[idx]
            if evens:
                res += sum(j < idx for j in evens)
            del prefix[idx]
    return res