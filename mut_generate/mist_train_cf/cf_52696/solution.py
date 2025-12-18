"""
QUESTION:
Write a function `is_prime(num)` that determines if a given number is prime and identifies its smallest non-trivial factor if it is not. The function should return a tuple `(True, None)` if the number is prime; otherwise, it should return `(False, factor)`, where 'factor' is the smallest non-trivial factor of the number. The function should handle numbers less than 2 correctly and should not iterate beyond the square root of the number when checking for factors.
"""

def entrance(num):
  if num < 2:
    return (False, None)
  for i in range(2, int(num**0.5)+1):
    if num % i == 0:
      return (False, i)
  return (True, None)