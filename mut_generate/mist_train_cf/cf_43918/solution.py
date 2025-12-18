"""
QUESTION:
Write a function named `findLHS` that takes an integer array `nums` as input and returns the length of its longest harmonious subsequence among all its possible subsequences. A harmonious array is defined as an array where the difference between its maximum value and its minimum value is exactly 1, and the subsequence should not contain any repeating sequence of numbers. The input array `nums` has the following constraints: `1 <= nums.length <= 2 * 10^4` and `-10^9 <= nums[i] <= 10^9`.
"""

from collections import Counter

def findLHS(nums):
    counter = Counter(nums)
    ans = 0
    for num in counter:
        if num + 1 in counter:
            ans = max(ans, counter[num] + counter[num + 1])
    return ans