"""
QUESTION:
Create a function `square_and_sort(arr)` that takes an array of integers as input, squares each number in the array, handles negative input values by returning their squares as positive numbers, and returns the resulting array sorted in ascending order.
"""

def square_and_sort(arr):
  """
  This function takes an array of integers, squares each number, 
  handles negative input values by returning their squares as positive numbers, 
  and returns the resulting array sorted in ascending order.
  
  Parameters:
  arr (list): A list of integers
  
  Returns:
  list: A list of squared integers sorted in ascending order
  """
  return sorted([abs(num)**2 for num in arr])