"""
QUESTION:
Write a function named `compute_lcm` that takes two positive integers `x` and `y` as input and returns their Least Common Multiple (LCM). The function should be efficient and correctly handle cases where `x` and `y` are of different orders of magnitude.
"""

def compute_lcm(x, y):
   if x > y:
       larger = x
   else:
       larger = y

   lcm = (x*y) // larger
   while True:
       if lcm % x == 0 and lcm % y == 0:
           return lcm
       lcm += 1