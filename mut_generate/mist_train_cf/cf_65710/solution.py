"""
QUESTION:
Design a function named `extract_num` that takes a string `s` as input and returns a list of integers. The function should extract numeric characters from the string, grouping consecutive digits together, and ignoring non-digit characters. The numbers in the output list should be in the order of their appearance in the string. The input string may contain spaces and non-digit characters. The function should be able to handle strings with multiple groups of consecutive digits.
"""

def extract_num(s): 
  temp = []
  num = ''
  for i in s:
    if i.isdigit():
      num += i
    elif num:
      temp.append(int(num))
      num = ''
  if num:
    temp.append(int(num))
  return temp