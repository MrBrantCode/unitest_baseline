"""
QUESTION:
Write a function `prime_fib_product(start, end)` that calculates the product of all prime Fibonacci numbers within a given interval `[start, end]`. The function should handle edge cases where the interval contains a single number or is invalid (i.e., `start` is greater than `end` or `start` is less than 0). The function should return the product of prime Fibonacci numbers as an integer, or the string "Invalid Range" for invalid intervals.
"""

from math import sqrt
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fib(n):
  if n < 2:
    return n
  else:
    return fib(n-1) + fib(n-2)

def is_prime(n):
  if n == 0 or n == 1:
    return False
  else:
    for i in range(2, int(sqrt(n)) + 1):
      if n % i == 0:
        return False
    return True

def prime_fib_product(start, end):
  if start > end or start < 0:
    return "Invalid Range"
  product = 1
  i = 0
  while fib(i) <= end:
    if fib(i) >= start and is_prime(fib(i)):
      product *= fib(i)
    i += 1
  return product