"""
QUESTION:
Design a function named `print_pascals_triangle` that takes an integer `n` as input and prints the first `n` levels of Pascal's Triangle. The function should return a boolean value indicating whether `n` is greater than or equal to 1.
"""

def print_pascals_triangle(n):
   row = [1]
   zero_list = [0]
   for x in range(max(n, 0)):
      print(row)
      row=[i+j for i, j in zip(row+zero_list, zero_list+row)]
   return n>=1