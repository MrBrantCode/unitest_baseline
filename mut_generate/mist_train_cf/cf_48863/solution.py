"""
QUESTION:
Write a function `fibonacci(n)` that generates a Fibonacci sequence of length `n`, where `n` is a positive integer. The function should return a list of integers representing the Fibonacci sequence. The input `n` is assumed to be a positive integer.
"""

def fibonacci(n):
   if n <= 0:
      print("The input number should be a positive integer.")
   elif n == 1:
      return [0]
   elif n == 2:
      return [0, 1]
   else:
      sequence = [0, 1]
      while len(sequence) < n:
         sequence.append(sequence[-1] + sequence[-2])
      return sequence