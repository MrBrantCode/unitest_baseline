"""
QUESTION:
Implement a function `weighted_average_sqrt(array)` that calculates the weighted average of the square roots of all numbers in the input array, where the weight assigned to the square root of each number is the number itself. The function should return the weighted average as a float value. The input array is a list of non-negative integers.
"""

import math

def weighted_average_sqrt(array):
  # Calculate the sum of all weights
  total_weight = sum(array)
  
  # Calculate the sum of square roots times their weights
  sum_weighted_sqrt = sum(math.sqrt(num) * num for num in array)
  
  # Calculate the average
  average = sum_weighted_sqrt / total_weight

  return average