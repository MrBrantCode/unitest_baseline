"""
QUESTION:
Create a function `maxSubArraySum` that takes an array of integers as input and returns the maximum sum of a contiguous sub-array within the given array. The function should handle arrays with both positive and negative integers.
"""

def maxSubArraySum(A):
   max_current = max_overall = A[0]
   for i in range(1,len(A)):
      max_current = max(A[i], max_current + A[i])
      max_overall = max(max_overall,max_current)
   return max_overall