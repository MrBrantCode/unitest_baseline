"""
QUESTION:
Develop a function named `nth_nonagonal` that takes a positive integer `n` as input and returns the nth term in the sequence of nonagonal numbers, where each nonagonal number is calculated using the formula `n(7n-5)/2`. The function should return an integer result.
"""

def nth_nonagonal(n):
  return n*(7*n-5)//2