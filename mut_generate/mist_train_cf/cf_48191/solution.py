"""
QUESTION:
Write two functions, `get_string_elements(data_list)` and `count_ending_with_e(data_list)`, to identify strings within a list that terminate with the English language vowel 'e'. The `get_string_elements(data_list)` function should filter out non-string elements from the list and return a list of strings. The `count_ending_with_e(data_list)` function should count the number of strings that end with 'e'. 

Do not use built-in function names for variable or function parameters. The input list may contain strings, integers, and floats.
"""

def get_string_elements(data_list):
  string_list = []
  for i in data_list:
    if type(i) == str:
      string_list.append(i)
  return string_list

def count_ending_with_e(string_list):
  count = 0
  for word in string_list:
    if word[-1].lower() == 'e':
      count += 1
  return count