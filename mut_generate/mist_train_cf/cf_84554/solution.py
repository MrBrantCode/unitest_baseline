"""
QUESTION:
Write a function called `find_intersection` that takes two lists of integers as input and returns their intersection as a new list in ascending order. The input lists can be of any length, can contain numbers in any order, and the numbers can range from -10,000 to 10,000. The function should be able to handle cases where the two lists have some or no common elements.
"""

def find_intersection(list_one, list_two):
  # Convert the arrays to sets
  set_one = set(list_one)
  set_two = set(list_two)
  
  # Find the intersection of the two sets
  intersection = set_one & set_two 
  
  # Convert the intersection set to a list and sort it
  sorted_list = sorted(list(intersection))
  
  return sorted_list