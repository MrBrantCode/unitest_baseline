"""
QUESTION:
Write a function `rhombus_area(rhombus_list)` that takes a list of tuples representing the lengths of the diagonals (d1, d2) of each rhombus. The function should return a list of the areas of these rhombuses, calculated using the formula: Area = (d1*d2)/2. Handle the case where the list of rhombuses is empty.
"""

def rhombus_area(rhombus_list):
  if not rhombus_list:
    return []
  else:
    return [(d1*d2)/2 for d1, d2 in rhombus_list]