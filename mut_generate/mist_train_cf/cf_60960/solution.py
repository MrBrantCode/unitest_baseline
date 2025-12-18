"""
QUESTION:
Write a function `find_average(num1, num2)` that calculates the average of two numbers. The function should only accept integers or floats as inputs. If either input is not a number, return the error message "Error: Both inputs must be numbers".
"""

def find_average(num1, num2): 
  if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
    return "Error: Both inputs must be numbers"
  total = num1 + num2
  average = total / 2 
  return average