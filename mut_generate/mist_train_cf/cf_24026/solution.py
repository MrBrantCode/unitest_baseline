"""
QUESTION:
Create a function `get_highest_prime(numbers)` that takes a list of integers as input and returns the highest prime number in the list. If no prime number exists, return 0. The function should only consider positive integers as prime numbers and handle cases where the input list contains non-positive integers or non-integer values.
"""

def get_highest_prime(numbers):
  highest_prime = 0
  for num in numbers:
    if isinstance(num, int) and num > 0:
      for i in range(2, num): 
        if (num % i == 0): 
          break
      else:
        highest_prime = max(highest_prime, num)
  return highest_prime