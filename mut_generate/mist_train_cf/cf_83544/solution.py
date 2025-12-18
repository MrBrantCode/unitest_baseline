"""
QUESTION:
Create a function called `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function should handle integers of all values, but note that prime numbers are greater than 1.
"""

def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True