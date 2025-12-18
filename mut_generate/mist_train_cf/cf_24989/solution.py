"""
QUESTION:
Implement a function `subsetsum(arr, target)` that uses a Greedy Algorithm to find a subset of the given array `arr` with the maximum sum that does not exceed the `target` sum. The function should return the subset of `arr` that meets this condition. Assume that `arr` is a list of non-negative integers and `target` is a non-negative integer.
"""

def subsetsum(arr, target):
  arr.sort() 
  n = len(arr) 
  sum = 0
  result = [] 
  
  for i in range(n):
    if ( sum + arr[i] <= target):
      result.append(arr[i])
      sum = sum + arr[i]
  
  return result