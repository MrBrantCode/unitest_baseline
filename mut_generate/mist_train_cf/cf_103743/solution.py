"""
QUESTION:
Write a function `average_even_elements` that calculates and returns the average of the even elements in a given array. The function should iterate through the array, sum up the even elements, and count the number of even elements. The function should then return the average by dividing the total sum by the count. The array may contain both positive and negative integers.
"""

def average_even_elements(arr):
  """
  This function calculates and returns the average of the even elements in a given array.
  
  Parameters:
  arr (list): A list of integers.
  
  Returns:
  float: The average of the even elements in the array.
  """
  total = 0
  count = 0
  for num in arr:
    if num % 2 == 0:
      total += num
      count += 1
  
  if count == 0:
    return 0  # or raise an exception, depending on the desired behavior
  return total / count