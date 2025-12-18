"""
QUESTION:
Design a function called `fibonacci` that calculates the nth Fibonacci number using recursion. The function should take an integer `n` as input, handle edge cases such as negative numbers and non-integer inputs, and achieve efficient time complexity by avoiding redundant calculations. The Fibonacci sequence is defined as follows: `fibonacci(0) = 0`, `fibonacci(1) = 1`, and `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)` for `n > 1`.
"""

def fibonacci(n, computed = {0: 0, 1: 1}):
  """
  Calculate the nth Fibonacci number using recursion with memoization.

  Args:
    n (int): A positive integer.
    computed (dict): A dictionary to store computed Fibonacci numbers (default: {0: 0, 1: 1}).

  Returns:
    int: The nth Fibonacci number if n is a positive integer, otherwise an error message.
  """

  # Check if input is a positive integer
  if type(n) != int or n < 0:
    return "Input should be a non-negative integer"

  if n not in computed:
    computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
  return computed[n]