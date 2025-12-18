"""
QUESTION:
Develop a function named `remove_duplicates` that takes an input list and returns the list with duplicates removed. The function should utilize recursion and the map() function. It should not use built-in functions like set(), the in keyword, or traditional looping constructs like for or while. Implement the function to compare elements without using any(), in, or similar functions.
"""

def remove_duplicates(input_list):
  if len(input_list) == 0:
    return []
  elif len(input_list) == 1:
    return input_list
  else:
    return list(map(
        lambda x: remove_duplicates(x) if isinstance(x, list) else x,
        [input_list[i] for i in range(len(input_list)) if input_list[i] not in input_list[:i]]
    ))