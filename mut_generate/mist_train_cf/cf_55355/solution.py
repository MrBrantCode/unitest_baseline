"""
QUESTION:
Write a function named `lcm` that takes three prime numbers `x`, `y`, and `z` as input and returns their Least Common Multiple (LCM). The input numbers must satisfy the constraints: `1 <= x, y, z <= 10^9`. The function should be computationally efficient to handle large inputs.
"""

def gcd(x, y):
  """ 
  Computes the greatest common divisor of two numbers using the Euclid's algorithm.
  """
  while(y): 
    x, y = y, x % y 
  return x

def lcm(x: int, y: int, z: int):
  """ 
  LCM determination function for x, y and z. 

  Constraints: x, y, z are prime numbers; 1 <= x, y, z <= 10^9
  """
  temp_lcm = (x * y) // gcd(x, y)
  return (temp_lcm * z) // gcd(temp_lcm, z)