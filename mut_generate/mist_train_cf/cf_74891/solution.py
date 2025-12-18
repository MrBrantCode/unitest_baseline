"""
QUESTION:
Write a function named `compute_hcf` that takes two integers `x` and `y` as input and returns their highest common factor. The function should work correctly even if the inputs are negative, and it should return the absolute value of the non-zero number if either input is zero.
"""

def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return abs(x)