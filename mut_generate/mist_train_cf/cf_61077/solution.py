"""
QUESTION:
Create a Python generator function `prime_numbers(n)` that yields prime numbers between `n^2` and `2n^2` (inclusive). The function should take an integer `n` as input and use a helper function to check for primality.
"""

import math

def is_prime(n):
  if n <= 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  m = int(math.sqrt(n))
  for i in range(3, m + 1, 2):
    if n % i == 0:
      return False
  return True

def prime_numbers(n):
  for num in range(n**2, 2*(n**2)+1):
    if is_prime(num):
      yield num