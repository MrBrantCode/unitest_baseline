"""
QUESTION:
Write a function named `fibonacci` that generates the Fibonacci sequence up to the nth number and returns it as a list. The function should take an integer `n` as input, where `n` is the number of elements in the Fibonacci sequence to generate. The function should be implemented using a loop structure, and the solution should be as concise as possible.
"""

def fibonacci(n):
  fib_seq = [0, 1]
  while len(fib_seq) < n:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])
  return fib_seq[:n]