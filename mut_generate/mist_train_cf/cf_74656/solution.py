"""
QUESTION:
Write a function `calc_median` that takes a list of floating-point numbers as input and returns the median of the numbers in the list. The function should be able to handle extremely large datasets efficiently. The input list is not guaranteed to be sorted.
"""

def calc_median(numbers):
  # Sort the list in ascending order
  numbers.sort()

  # Compute the median
  if len(numbers) % 2 == 0:
    # If length is even, median is average of two middle numbers
    median1 = numbers[len(numbers)//2]
    median2 = numbers[len(numbers)//2 - 1]
    median = (median1 + median2)/2
  else:
    # If length is odd, median is the middle number
    median = numbers[len(numbers)//2]
  
  return median