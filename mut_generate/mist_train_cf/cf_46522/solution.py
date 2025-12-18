"""
QUESTION:
Parse the input list of characters and extract their names and professions. Write a function named `parse_data` that takes a list of strings representing characters in the format "Name (Profession)" and returns a list of dictionaries with keys 'name' and 'occupation'. The function should handle multiple characters.
"""

import re

def parse_data(inputs):
  parsed_data = []
  pattern = r"([^()]+) \(([^()]+)\)"

  for i in inputs:
    match = re.findall(pattern, i)
    for m in match:
      parsed_data.append({'name': m[0].strip(), 'occupation': m[1].strip()})

  return parsed_data