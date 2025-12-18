"""
QUESTION:
Find the first prime number in an array that is greater than 10. Implement a function `find_first_prime_greater_than_10` that takes an array of integers as input, and returns the first prime number in the array that is greater than 10. If no such number exists, the function should return None.
"""

def find_first_prime_greater_than_10(array):
  def is_prime(n):
    if n <= 1:
      return False
    if n <= 3:
      return True
    if n % 2 == 0 or n % 3 == 0:
      return False
    i = 5
    while(i * i <= n):
      if n % i == 0 or n % (i + 2) == 0:
        return False
      i += 6
    return True

  for num in array:
    if num > 10 and is_prime(num):
      return num
  return None