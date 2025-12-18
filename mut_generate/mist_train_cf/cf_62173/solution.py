"""
QUESTION:
Create a function `cube_and_sum` that takes a one-dimensional matrix (list of integers) as input and returns a boolean value. The function should calculate the sum of the cube of each element in the matrix without using any inbuilt method for cube calculation, then check if the sum is a prime number. If the sum is prime, return `True`, otherwise return `False`. The function should be efficient and only iterate up to the square root of the number when checking for primality.
"""

def cube_and_sum(matrix):
  def calculate_sum(matrix):
    sum_value = sum([ele**3 for ele in matrix])
    return sum_value

  def check_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
      return False
    for i in range(3, int(n**0.5) + 1, 2):
      if n % i == 0:
        return False
    return True

  sum_value = calculate_sum(matrix)
  return check_prime(sum_value)