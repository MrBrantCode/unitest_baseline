"""
QUESTION:
Create a function called `reverse_list` that takes a list as input and returns the reversed list. The function should not use any built-in reverse functions or methods and should instead use a for loop. The input list should not be modified during the iteration process.
"""

def reverse_list(input_list):
  output = []
  for i in range(len(input_list)):
    output.append(input_list[len(input_list)-1-i])
  return output