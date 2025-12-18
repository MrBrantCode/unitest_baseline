"""
QUESTION:
Write a function `maxSubArraySum(a)` that takes an array of integers `a` as input and returns the largest possible sum of a contiguous subarray within `a`. The function should have a time complexity of O(n), where n is the length of the array.
"""

def maxSubArraySum(a): 
  size = len(a) 
  max_so_far = a[0] 
  current_max = a[0] 
  for i in range(1, size): 
      current_max = max(a[i], current_max + a[i]) 
      max_so_far = max(max_so_far, current_max) 
  return max_so_far