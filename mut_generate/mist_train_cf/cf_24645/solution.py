"""
QUESTION:
Create a function named `difference_array` that takes two array-like structures, `list_1` and `list_2`, as input. The function should return a new array containing all elements from `list_1` that do not appear in `list_2`.
"""

def difference_array(list_1, list_2):
  """
  Returns a new array containing all elements from list_1 that do not appear in list_2.
  
  Parameters:
  list_1 (list): The list to find unique elements from.
  list_2 (list): The list to compare against.
  
  Returns:
  list: A new list containing unique elements from list_1.
  """
  new_list = []
  for i in list_1:
    if i not in list_2:
      new_list.append(i)
  return new_list