"""
QUESTION:
Implement a function called `reverse_list` that takes a list of strings as input, reverses the order of its elements, and returns the reversed list. The function should not use any built-in reverse functions. It should also validate the input data to ensure all elements are strings, raising an exception if any non-string element is found.
"""

def reverse_list(input_list):
  for item in input_list:
    if not isinstance(item, str):
      raise Exception("Invalid data: list contains non-string element.")
  
  reversed_list = []
  for i in range(len(input_list) - 1, -1, -1):
    reversed_list.append(input_list[i])
  
  return reversed_list