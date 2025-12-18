"""
QUESTION:
Implement a function called gcd that takes two numbers as parameters and returns their greatest common divisor. The function should be recursive.
"""

def gcd(a, b): 
  """
  This function calculates the greatest common divisor of two numbers using recursion.
  
  Parameters:
  a (int): The first number.
  b (int): The second number.
  
  Returns:
  int: The greatest common divisor of a and b.
  """
  if a == 0: 
    return b 
  return gcd(b % a, a)