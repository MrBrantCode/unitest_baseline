"""
QUESTION:
Write a function `find_max` that uses recursion to find the maximum value in a given numeric array. The array contains only integers, and the function should return the maximum value. The array length is unknown but will contain at least one element.
"""

def find_max(arr): 
  # Base case 
  if len(arr) == 1: 
      return arr[0] 
  else: 
      max_n = find_max(arr[1:]) 
      # Compare the maximum element with the first element of the array 
      if arr[0] > max_n: 
          return arr[0] 
      else: 
          return max_n 