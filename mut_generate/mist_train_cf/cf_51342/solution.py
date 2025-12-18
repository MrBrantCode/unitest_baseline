"""
QUESTION:
Write a function `fibonacci_quadruplet` that takes an array of integers `arr` as input and returns `True` if the array contains a sequence of four consecutive Fibonacci numbers and `False` otherwise.

The length of `arr` is at least 1 and at most 1000, and each element in `arr` is an integer between 1 and 1000, inclusive.
"""

def fibonacci_quadruplet(arr):
  fib_set = set()
  a, b = 0, 1
  while a <= 1000:
    fib_set.add(a)
    a, b = b, a + b
  seq = 0
  for num in arr:
    if num in fib_set:
      seq += 1
      if seq >= 4:
        return True
    else:
      seq = 0
  return False