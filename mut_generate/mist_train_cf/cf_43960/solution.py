"""
QUESTION:
Develop a function named `compute_hcf` that takes two integers as input and returns their highest common factor (HCF), also known as the greatest common divisor (GCD). The function should use the Euclidean algorithm.
"""

def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x