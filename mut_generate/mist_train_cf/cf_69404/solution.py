"""
QUESTION:
Develop a function named `discrepancy(n)` that calculates the discrepancy between the cumulative sum of cubes for the initial `n` natural numbers and the cumulative sum of these initial `n` natural numbers. The function should be implemented using recursive techniques without employing any pre-existing Python functions or libraries.
"""

def discrepancy(n):
  if n == 1:
    return 0
  else:
    return (n * n * n) - n + discrepancy(n-1)