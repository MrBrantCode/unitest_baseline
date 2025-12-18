"""
QUESTION:
Create a function named `calc_gcd` that takes two integers `a` and `b` as input and returns their Greatest Common Denominator (GCD). The function should be able to handle very large numbers without overflowing.
"""

def calc_gcd(a, b):
  while(b): 
    a, b = b, a % b 
  return a