"""
QUESTION:
Create a function called `factorial` that calculates the factorial of a given integer `n`. The function should use recursion to calculate the factorial and include a base case to stop the recursion.
"""

def factorial(n):
  if n == 0:    
    return 1
  else:         
    return n * factorial(n-1)