"""
QUESTION:
Write a function `find_divisible_numbers` that finds all numbers divisible by 5 but not a multiple of 7 within a given range. The function should take two parameters: `start` and `end`, representing the start and end of the range (inclusive). The function should return a list of numbers that meet the specified conditions.
"""

def find_divisible_numbers(start, end):
  """
  Finds all numbers divisible by 5 but not a multiple of 7 within a given range.
  
  Args:
    start (int): The start of the range (inclusive).
    end (int): The end of the range (inclusive).
  
  Returns:
    list: A list of numbers that meet the specified conditions.
  """
  return [i for i in range(start, end+1) if i % 5 == 0 and i % 7 != 0]