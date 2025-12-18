"""
QUESTION:
Create a function named `is_prime(n)` that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(n):
  """Check if a number is prime."""
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True