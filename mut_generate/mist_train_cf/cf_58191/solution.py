"""
QUESTION:
Write a function `lucas` that generates the Lucas number sequence in reverse order, where the Lucas sequence starts with 2 and 1 instead of 0 and 1, and then use this function to print the sequence from the 12th term to the 1st term.
"""

def lucas(n): 
    a, b = 2, 1
    if n == 0: 
      return a
    elif n == 1: 
      return b 
    else: 
      for i in range(2,n+1): 
        c = a + b
        a, b = b, c
      return b