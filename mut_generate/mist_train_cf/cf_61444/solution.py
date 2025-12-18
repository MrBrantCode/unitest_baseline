"""
QUESTION:
Write a function named `find_primes` that takes a list of integers, which may contain up to three levels of nested lists, and returns a list of prime numbers found within the given list. The function should handle nested lists and optimize the prime number checking process by only checking divisibility up to the square root of the number.
"""

import math

def find_primes(num_list):
  primes = []

  def is_prime(num):
    if num < 2:
      return False
    for i in range(2, math.isqrt(num)+1):
      if (num % i) == 0:
        return False
    return True

  def helper(lst):
    for element in lst:
      if type(element) is list:
        helper(element)
      elif is_prime(element):
        primes.append(element)
  
  helper(num_list)
  return primes