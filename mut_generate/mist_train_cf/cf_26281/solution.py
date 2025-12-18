"""
QUESTION:
Design a function named `Fibonacci(n)` that generates the nth number in the Fibonacci sequence, where the Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should recursively calculate the nth Fibonacci number. The input `n` should be a non-negative integer. If `n` is less than 0, the function should print an error message.
"""

def Fibonacci(n): 
   if n<0: 
      print("Incorrect input") 
   # First Fibonacci number is 0 
   elif n==0: 
      return 0
   # Second Fibonacci number is 1 
   elif n==1: 
      return 1
   else: 
      return Fibonacci(n-1)+Fibonacci(n-2)