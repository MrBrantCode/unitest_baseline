"""
QUESTION:
Create a function called `calculate_std_dev` that takes a list of 7 numbers as input and returns the standard deviation of the numbers. The function should not use any external libraries for calculating the standard deviation, but instead implement it manually using the formula for sample standard deviation. The input list is assumed to contain only numbers.
"""

def calculate_mean(data):
  return sum(data) / len(data)

def calculate_variance(data):
  mean = calculate_mean(data)
  return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

def calculate_std_dev(data):
  return calculate_variance(data) ** 0.5