"""
QUESTION:
Design a recursive function named `Fibonacci_Word` that calculates the m-th Fibonacci word in the Fibonacci word sequence. The Fibonacci word sequence is a series where each word is formed by concatenating the previous two words, starting with '0' and '1'. The function should take an integer `n` as input and return the corresponding Fibonacci word.
"""

def Fibonacci_Word(n):
  if n == 0:
    return "0"
  elif n == 1:
    return "1"
  else:
    return Fibonacci_Word(n-1) + Fibonacci_Word(n-2)