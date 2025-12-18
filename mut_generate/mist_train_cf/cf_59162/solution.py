"""
QUESTION:
Write a function `findLHS` that takes an integer array `nums` as input and returns the length of its longest harmonious subsequence, where a harmonious subsequence is defined as a subsequence with no repeating sequence of numbers and the difference between the highest and lowest value is precisely 1. The length of the input array `nums` is between 1 and 2 * 10^4 (inclusive), and the values in `nums` are between -10^9 and 10^9 (inclusive).
"""

def findLHS(nums):
    from collections import Counter
    count = Counter(nums)
    return max([count[x] + count[x+1] for x in count if count[x+1]] or [0])