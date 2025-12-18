"""
QUESTION:
Find a pair of prime numbers in a given array that add up to a given number N. 

The function should be named `find_prime_pairs` and should take two parameters: `n` (the given number) and `nums` (the given array). The function should return a pair of prime numbers that add up to `n`, or `None` if no such pair exists. The solution should optimize for time complexity.
"""

def find_prime_pairs(n, nums):
  def prime_sieve(n):
    sieve = [True] * (n+1)
    p = 2
    while p * p <= n:
      if sieve[p] == True:
        for i in range(p * p, n+1, p):
          sieve[i] = False
      p += 1
    primes = [p for p in range(2, n) if sieve[p]]
    return primes

  primes = prime_sieve(n)
  primes_set = set(primes)
  for num in nums:
    if num in primes_set and n - num in primes_set:
      return num, n - num
  return None