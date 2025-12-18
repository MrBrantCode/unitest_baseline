"""
QUESTION:
Implement a function 'change' that takes an integer as input and returns a string message based on the sign and parity of the input number. The function should return specific messages for negative numbers, positive even numbers, positive odd numbers, and zero.
"""

def change(num):
  if num < 0:
    return "Test is a negative number"
  elif num > 0:
    if num % 2 == 0:
      return "Test is a positive even number"
    else:
      return "Test is a positive odd number"
  else:
    return "Test is zero"