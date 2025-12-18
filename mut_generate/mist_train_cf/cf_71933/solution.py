"""
QUESTION:
Create a function `cleaned_list` that takes a list of integers as input, removes negative integers, zeros, and integers greater than 10, removes duplicates, and returns a list of unique positive integers in the range of 1 to 10 in ascending order.
"""

def cleaned_list(input_list):
  new_set = set() 
  for i in input_list:
    if i >= 1 and i <= 10: 
      new_set.add(i) 
  return sorted(list(new_set)) 