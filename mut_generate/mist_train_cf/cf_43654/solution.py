"""
QUESTION:
Write a function named `find_max_pair` that takes a list of integers `nums` as input and returns a pair of integers with the maximum sum. The function should handle the case where the input list has less than two elements.
"""

def find_max_pair(nums):
  if len(nums) < 2:
    return "Not enough elements to form a pair"
  max1=max2=float('-inf')
  for num in nums:
    if num>max1:
      max2=max1
      max1=num
    elif num>max2:
      max2=num
  return max1, max2