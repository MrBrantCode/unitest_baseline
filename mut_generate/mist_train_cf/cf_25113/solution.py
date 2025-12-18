"""
QUESTION:
Create a function called `sum_squares(n)` that calculates the sum of the squares of all numbers from 1 to `n` (inclusive), where `n` is a positive integer. The function should return the total sum.
"""

def sum_squares(n): 
   total = 0
   for x in range(1,n+1): 
      total += x * x
   return total