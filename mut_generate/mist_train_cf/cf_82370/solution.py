"""
QUESTION:
Create a function named `square_and_prime_factors` that takes an integer `n` as input and returns a tuple. The first element of the tuple should be the square of `n`. If `n` is a prime number, the second element should be a list of prime factors of the square of `n`; otherwise, it should be `None`. Ensure the time complexity of the function is O(sqrt(n)).
"""

import math

def square_and_prime_factors(n):
  square_of_n = n**2
  if n <= 1 or (n % 2 == 0 and n > 2): 
    return (square_of_n, None)
  if not all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2)): 
    return (square_of_n, None)

  i = 2
  factors = []
  squared_n = square_of_n
  while i * i <= squared_n:
    if squared_n % i:
      i += 1
    else:
      squared_n //= i
      factors.append(i)
  if squared_n > 1:
    factors.append(squared_n)
  return (square_of_n, factors)