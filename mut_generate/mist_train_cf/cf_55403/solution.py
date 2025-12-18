"""
QUESTION:
Write a function named `compute_lcm` that takes an integer `n` and an array of `n` positive integers as input, and returns their lowest common multiple (LCM) without using any built-in LCM methods.
"""

def compute_lcm(n, arr):
   def compute_gcd(x, y):
       while(y):
           x, y = y, x % y
       return x

   lcm = arr[0]
   for i in range(1, n):
       lcm = lcm*arr[i]//compute_gcd(lcm, arr[i])
   return lcm