"""
QUESTION:
Create a function called `subarraySum` that takes an array of integers `nums` and an integer `k` as input. The function should return the total count of continuous subarrays whose sum is equivalent to `k`.

Restrictions: 
- The length of `nums` is between 1 and 2 * 10^4 (inclusive).
- The value of each element in `nums` is between -1000 and 1000 (inclusive).
- The value of `k` is between -10^7 and 10^7 (inclusive).
- All elements in `nums` and `k` are integers.
"""

def subarraySum(nums, k):
    count = 0
    for start in range(len(nums)):
        sum = 0
        for end in range(start, len(nums)):
            sum += nums[end]
            if sum == k:
                count += 1
    return count