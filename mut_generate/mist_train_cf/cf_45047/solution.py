"""
QUESTION:
Construct a function `find_and_multiply_prime_numbers` that takes one or more lists of integers as input. The function should return a list of tuples, where each tuple contains a list of prime numbers in ascending order and the product of these prime numbers. The function should handle inputs that are not integers, non-integer floating point numbers, and integers that exceed Python's maximum integer limit (if any). It should also process large inputs and multiple collections efficiently. The function should not include negative integers, zero, or non-prime numbers in its output.
"""

import math

def is_prime(n):
  if n in (0, 1):
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  sqrt_n = math.isqrt(n)
  for i in range(3, sqrt_n + 1, 2):
    if n % i == 0:
      return False
  return True

def find_and_multiply_prime_numbers(*input_lists):
  results = []
  for input_list in input_lists:
    try:
      prime_numbers = []
      product = 1
      for num in sorted([abs(int(x)) for x in input_list if isinstance(x, int) or (isinstance(x, float) and x.is_integer())]):
        if is_prime(num):
          prime_numbers.append(num)
          product *= num
      results.append((prime_numbers, product))
    except ValueError as e:
      print(f"Skipping invalid value: {e}")
  return results