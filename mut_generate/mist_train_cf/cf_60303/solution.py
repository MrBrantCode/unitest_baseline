"""
QUESTION:
Create a function called `sum_even_squares` that takes a list of integers as input and returns the sum of the squares of the even numbers in the list. The function should filter out the odd numbers and only consider the even numbers for the calculation.
"""

def sum_even_squares(numbers):
  return sum(n**2 for n in numbers if n%2 == 0)