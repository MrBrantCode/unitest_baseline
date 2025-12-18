"""
QUESTION:
Create a function called `prime_range` that takes an integer `n` as input and returns a tuple containing the total number of prime numbers and a list of all prime numbers between 2 and `n` (inclusive). The function should handle invalid inputs where `n` is less than 2, and it should be optimized for time and space complexity.
"""

def prime_range(n):
  if n<2:
    print("Invalid input! Please enter a number bigger than or equal to 2.")
    return []
  primes = [2] 
  for i in range(3, n+1, 2): 
    sqrt_i = int(i**0.5) + 1
    for j in range(2, sqrt_i):
      if (i % j) == 0:
        break
    else:
      primes.append(i)
  return len(primes), primes