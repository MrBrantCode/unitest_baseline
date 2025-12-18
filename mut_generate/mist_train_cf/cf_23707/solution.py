"""
QUESTION:
Write a recursive function named `recSum` that takes a single integer `n` as input and returns the sum of all integers from 1 to `n` inclusive.
"""

def recSum(n):
  if n == 1:
    return 1
  return n + recSum(n-1)