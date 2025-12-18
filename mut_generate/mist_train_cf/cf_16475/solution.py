"""
QUESTION:
Find the most frequent value in a list of numbers.

Write a function `find_most_frequent(nums)` that takes a list of numbers `nums` as input, where `nums` can contain integers, floats, and negative numbers, and returns the value that appears most frequently in the list. The list is guaranteed to contain at least one repeated value. The function should have a time complexity of O(n), where n is the length of the input list.
"""

from collections import defaultdict

def most_frequent(nums):
    count_dict = defaultdict(int)  # initialize an empty dictionary with default value 0
    
    for num in nums:
        count_dict[num] += 1
    
    max_count = 0
    most_frequent = None
    
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            most_frequent = num
    
    return most_frequent