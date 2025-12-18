"""
QUESTION:
Implement a function named `prime_factors(n)` that takes an integer `n` as an argument and returns a list of its prime factors in ascending order. The function should handle edge cases where `n` is negative or zero, and it should include repeated prime factors the correct number of times. The function should use a loop to compute the prime factors.
"""

def prime_factors(n):
  i = 2
  factors = []
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
      factors.append(i)
  if n > 1:
    factors.append(n)
  return sorted(factors)