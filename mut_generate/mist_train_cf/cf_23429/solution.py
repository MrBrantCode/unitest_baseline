"""
QUESTION:
Implement a function named `is_prime(number)` that determines whether a given number is prime or not. The function should return `True` if the number is prime and `False` otherwise. The function must work with positive integers.
"""

def is_prime(number):
  if number < 1:
    return False
  for check in range(2, number):
    if number % check == 0:
      return False
  return True