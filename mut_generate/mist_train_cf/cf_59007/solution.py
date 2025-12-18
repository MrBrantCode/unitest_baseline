"""
QUESTION:
Write a function `area(n)` to calculate the smallest possible area of a symmetrical convex grid polygon with `n` vertices. The function should take an integer `n` as input and return the calculated area. The area should be rounded to the nearest integer as it cannot be a fraction of a unit.
"""

def area(n):
  return round(n * ((n / 4) + 0.75) / 2)