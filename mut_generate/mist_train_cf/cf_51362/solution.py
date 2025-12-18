"""
QUESTION:
Create a function `generate_prime_dict(n)` that generates a dictionary where the keys are the first 'n' prime numbers and their corresponding values are their squares. The function should be scalable to work with any given 'n'.
"""

def generate_prime_dict(n):
  """Generate a dictionary with the first 'n' prime numbers as keys and their squares as values."""
  primes = []
  i = 2
  while len(primes) < n:
    for p in primes:
      if i % p == 0:
        break
    else:
      primes.append(i)
    i += 1
  return {p: p**2 for p in primes}