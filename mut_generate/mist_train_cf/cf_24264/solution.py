"""
QUESTION:
Create a function named `add_numbers` that takes two integers as input and returns their sum without using the addition operator (+). Implement this function using bitwise operations.
"""

def add_numbers(a, b):
  while b != 0:
    carry = a & b
    a = a ^ b
    b = carry << 1
  return a