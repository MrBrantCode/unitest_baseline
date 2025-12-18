"""
QUESTION:
Write a function `prime_numbers` that takes a list of integers as input and returns a list of prime numbers from the input list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should check for prime numbers efficiently by only checking divisibility up to the square root of each number.
"""

import math

def prime_numbers(lst):
  primes = []
  for num in lst:
    if num > 1:
      for i in range(2, math.isqrt(num) + 1):
        if (num % i) == 0:
          break
      else:
        primes.append(num)
  return primes