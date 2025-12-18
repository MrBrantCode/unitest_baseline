"""
QUESTION:
Create a function named `fibonacci` that takes an integer `n` as input and returns the `n`-th ordinal number in the Fibonacci sequence. The function should use an iterative approach and handle edge cases where `n` is not a positive integer.
"""

def fibonacci(n):
  # handle edge cases
  if not isinstance(n, int) or n <= 0:
    return "Incorrect input"

  a, b = 0, 1 
  for _ in range(n):
    a, b = b, a + b
  return a