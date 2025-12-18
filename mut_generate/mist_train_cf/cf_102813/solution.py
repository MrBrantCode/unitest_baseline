"""
QUESTION:
Write a function named `most_frequent_value` that takes a list of integers as input and returns the integer that appears most frequently. The input list will always contain at least one repeated value. The function should be able to handle any list of integers.
"""

from collections import Counter

def most_frequent_value(nums):
    counter = Counter(nums)
    return counter.most_common(1)[0][0]