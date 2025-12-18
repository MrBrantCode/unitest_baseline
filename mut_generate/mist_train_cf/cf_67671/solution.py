"""
QUESTION:
Create a function `advanced_squares_dictionary` that takes a list of numbers as input and returns a dictionary where each key is a number from the input list and its corresponding value is a tuple containing the square of the number and the reciprocal of the square. If the number is zero, its corresponding value should be `None`.
"""

def advanced_squares_dictionary(numbers):
  return {num: (num ** 2, 1 / (num ** 2)) if num != 0 else None for num in numbers}