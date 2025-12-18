"""
QUESTION:
Write a function `fibonacci(n)` to generate the Fibonacci sequence up to `n` numbers using Binet's Formula, taking into account rounding errors due to the usage of the golden ratio and its reciprocal. Also, implement a function `is_fibonacci(num)` to check if a given number `num` is part of the Fibonacci series or not. The functions should only use the golden ratio and its reciprocal in the calculation.
"""

import math

# Golden ratio
phi = (1 + math.sqrt(5))/2
# Reciprocal of golden ratio
reci_phi = -1/phi

# Check if a given number can be written as 5*n*n - 4 or 5*n*n + 4.
# If yes, then the number is part of the Fibonacci series.
def is_fibonacci(num):
  return (math.sqrt(5*num*num - 4) % 1 == 0) or (math.sqrt(5*num*num + 4) % 1 == 0)

def fibonacci(n):
  fib_series = []
  for i in range(n):
    # Binet's formula
    fib_value = (pow(phi, i) - pow(reci_phi, i))/math.sqrt(5)
    fib_value = round(fib_value) 
    fib_series.append(fib_value)
  return fib_series