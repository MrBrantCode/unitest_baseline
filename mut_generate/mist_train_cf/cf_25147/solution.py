"""
QUESTION:
Create a function named `gcd(a, b)` that calculates the Greatest Common Divisor of two integers `a` and `b` using recursion. Ensure the function works correctly even if `a` or `b` (but not both) is zero.
"""

def gcd(a, b):
  if a == 0:
    return b
  if b == 0:
    return a

  if a > b:
    return gcd(a % b, b)
  else:
    return gcd(a, b % a)