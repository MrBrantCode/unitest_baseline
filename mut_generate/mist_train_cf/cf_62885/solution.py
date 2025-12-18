"""
QUESTION:
Function: `maxEqualFreq(nums)`

Given an array `nums` composed of positive integers, find the longest possible length of a prefix of `nums` that allows for the removal of exactly one element, resulting in every number that has appeared in the prefix having the same frequency of occurrence. Return a list containing the maximum prefix length and the smallest number removed to achieve this maximum equal frequency.

Restrictions:
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
"""

from collections import Counter, defaultdict
def maxEqualFreq(nums):
    count = Counter()
    freq = defaultdict(int)
    max_count = res = 0
    
    for i, x in enumerate(nums, 1):
        freq[count[x]] -= 1
        count[x] += 1
        freq[count[x]] += 1
        max_count = max(max_count, count[x])
        
        if max_count * freq[max_count] == i - 1 and i < len(nums):
            res = i
        if max_count * (freq[max_count] - 1) + max_count - 1 == i:
            res = i
            
    return [res, nums[res-1]] if res > 0 else [0, -1]