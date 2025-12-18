"""
QUESTION:
Create a function called `create_list(n)` that generates a list of numbers from 0 to n-1, where n is a given integer. The function should return the generated list.
"""

def create_list(n):
  result = [] 
  for i in range(0,n): 
    result.append(i) 
  return result