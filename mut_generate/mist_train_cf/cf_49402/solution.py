"""
QUESTION:
Write a Python function `check_number_properties` that takes an integer `num` as input and returns a string describing whether the number is even, odd, or zero, and whether it's prime or not. The function should handle all possible integer inputs.
"""

def check_number_properties(num):
  even_odd = "Zero" if num == 0 else "Even" if num % 2 == 0 else "Odd"
  is_prime = "Prime" if num > 1 and all(num % i for i in range(2, num)) else "not Prime"
  return f'The number is {even_odd} and {is_prime}'