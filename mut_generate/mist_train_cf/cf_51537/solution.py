"""
QUESTION:
Write a function `partition_list(nums)` that takes a list of integers `nums` as input and returns a list of two lists. The first inner list should contain the even integers from `nums` sorted in ascending order, and the second inner list should contain the odd integers from `nums` sorted in descending order. Optimize the function for time complexity.
"""

def partition_list(nums):
      evens = sorted([x for x in nums if x % 2 == 0])
      odds = sorted([x for x in nums if x % 2 != 0], reverse=True)
      return [evens, odds]