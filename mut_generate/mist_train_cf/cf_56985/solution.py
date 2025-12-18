"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of strings as an argument and returns a new list with all duplicates removed, preserving the original order.
"""

def remove_duplicates(my_list):
  seen = set()
  result = [x for x in my_list if not (x in seen or seen.add(x))]
  return result