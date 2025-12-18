"""
QUESTION:
Create a function named `fibonacci(n)` that generates the Fibonacci sequence up to the nth term, where n is a non-negative integer. The function should return a list of integers representing the sequence.
"""

def fibonacci(n):
   sequence = []
   a, b = 0, 1
   while len(sequence) < n:
       sequence.append(a)
       a, b = b, a + b
   return sequence