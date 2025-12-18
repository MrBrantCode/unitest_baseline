"""
QUESTION:
Write a function named `replace_element` that takes three arguments: an array, an index, and a new value. The function should replace the element at the specified index in the array with the new value and return the modified array. If the index is out of the array's range, return 'Error: Invalid index'.
"""

def replace_element(array, index, new_value):
  if index < 0 or index >= len(array):
    return 'Error: Invalid index'
  else:
    array[index] = new_value
    return array