"""
QUESTION:
Create a function sumToN that takes a single positive integer n as input and returns the sum of all integers from 1 to n. The function should return an integer.
"""

def sumToN(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  return sum