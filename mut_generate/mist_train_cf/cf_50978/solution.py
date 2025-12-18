"""
QUESTION:
Write a function `find_most_uncommon_symbol(s)` that takes a string `s` of ASCII symbols as input and returns the symbol with the most uncommon hexadecimal value. If multiple symbols have the same lowest count, return the one with the least hexadecimal value.
"""

def find_most_uncommon_symbol(s):
  char_dict = {}

  # tally the hexadecimal values
  for char in s:
    char_hex_val = hex(ord(char))
    if char_hex_val in char_dict:
      char_dict[char_hex_val]["count"] += 1
    else:
      char_dict[char_hex_val] = {"count": 1, "char": char}
  
  # find the most uncommon hexadecimal value
  min_count = float("inf")
  least_hex_char = ""
  least_hex_value = None
  for char_hex_value, char_info in char_dict.items():
    if char_info["count"] < min_count:
      min_count = char_info["count"]
      least_hex_char = char_info["char"]
      least_hex_value = char_hex_value
    elif char_info["count"] == min_count and char_hex_value < least_hex_value: # if tie, get the one with least hex value
      least_hex_char = char_info["char"]
      least_hex_value = char_hex_value

  return least_hex_char