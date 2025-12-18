"""
QUESTION:
Design a function `sum_except_self` that takes a list of integers as input and returns a new list where each element is the sum of all numbers from the initial list, excluding the number at the same index. The function must handle negative numbers and should reject lists where any number appears more than twice, returning None in such cases.
"""

from collections import Counter

def sum_except_self(nums):
    counts = Counter(nums)
    if any(count > 2 for count in counts.values()):
        return None

    total_sum = sum(nums)
    return [total_sum - num for num in nums]