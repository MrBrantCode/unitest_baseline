"""
QUESTION:
Given an integer array `arr`, write a function `trimMean(arr)` that returns the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements. If the smallest 5% and the largest 5% contain any duplicate numbers, remove all instances of these numbers from the array before calculating the mean.

Constraints: `20 <= arr.length <= 1000` and `arr.length` is a multiple of `20`. `0 <= arr[i] <= 105`.
"""

def trimMean(arr):
  n = len(arr)
  arr.sort()
  five_percent = int(n * 0.05)
  arr = arr[five_percent:-five_percent]
  return sum(arr) / len(arr)