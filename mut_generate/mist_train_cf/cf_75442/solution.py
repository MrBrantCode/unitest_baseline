"""
QUESTION:
Given a non-empty array of integers `nums`, every element appears three times except for one, which appears exactly once. Implement a function `singleNumber(nums)` that finds the single number with a linear runtime complexity and without using extra memory. The function should take an array of integers `nums` as input and return the single number.

Constraints: `1 <= nums.length <= 3 * 10^4` and `-3 * 10^4 <= nums[i] <= 3 * 10^4`.
"""

def singleNumber(nums):
    ans = 0
    for i in range(32):
        count = 0
        for num in nums:
            if ((num >> i) & 1):
                count += 1
        ans |= (count%3) << i
    if ans >= 2**31:
        ans -= 2**32
    return ans