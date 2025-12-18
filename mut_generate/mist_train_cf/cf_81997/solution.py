"""
QUESTION:
Write a function `solve` that takes a list of integers as input. The function should sort the list in descending order and return the sum of the top two highest values if the list has 5 or more elements. If the list has less than 5 elements, it should return the single highest value.
"""

def entrance(array):
  # Sort the array in descending order
  array.sort(reverse=True)
  
  # If the array has 5 or more elements, return the sum of the top two highest values
  if len(array) >= 5:
    return array[0] + array[1]
  
  # If the array has less than 5 elements, return the highest value
  else: 
    return array[0]