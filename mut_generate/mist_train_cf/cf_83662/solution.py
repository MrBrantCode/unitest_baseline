"""
QUESTION:
Write a function `sum_first_three` that takes a list of integers as input, removes duplicates, sorts the list in descending order without using built-in functions or libraries except for 'append' and 'len' functions, and returns the sum of the first three elements in the modified list.
"""

def sum_first_three(lst):
  # Remove duplicates from the list
  new_lst = []
  for num in lst:
    if num not in new_lst:
      new_lst.append(num)

  # Sort the list in descending order
  for i in range(len(new_lst)):
    for j in range(i + 1, len(new_lst)):
      if new_lst[i] < new_lst[j]:
        new_lst[i], new_lst[j] = new_lst[j], new_lst[i]

  # Return the sum of the first three elements in the modified list
  return sum(new_lst[:3])