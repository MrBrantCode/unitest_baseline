"""
QUESTION:
Write a function `most_common(nums)` that takes a list of integers `nums` as input, where `nums` has at least 2 unique values and a length between 2 and 10^5 (inclusive), and returns a list of tuples containing the most frequent value(s) and their count. If there is a tie for the most frequent value, return all such values.
"""

from collections import Counter

def most_common(nums):
    cnt = Counter(nums)
    max_count = max(cnt.values())
    return [(num, count) for num, count in cnt.items() if count == max_count]